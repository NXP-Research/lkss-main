import requests

from docutils import nodes

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxRole
from sphinx.util.typing import ExtensionMetadata

from sphinx.util import logging

REST_URL = "https://elixir.bootlin.com/api/ident/linux/{}?version=latest&family=C"
PATH_WHITELIST = (
	"arch/",
	"drivers/",
	"fs/",
	"include/",
	"kernel"
)

logger = logging.getLogger(__name__)

def get_lxr_url(symbol, location, symbol_type) -> str:
	reply = requests.get(REST_URL.format(symbol))
	reply.raise_for_status()

	url = "https://elixir.bootlin.com/linux/latest/source/"

	raw = reply.json().get("definitions")
	if not raw or raw is None:
		logger.warning(f"no LXR definitions for symbol {symbol}", location=location)
		return None

	# filter out all paths that don't start with include/
	# also, make sure the match is of the expected type
	match = None

	for entry in raw:
		if entry["path"].startswith(PATH_WHITELIST) and entry["type"] == symbol_type:
			if match is not None:
				logger.warning(f"multiple LXR definitions for symbol {symbol}", location=location)
				return None

			match = entry

	if match is None:
		logger.warning(f"no LXR definition for symbol {symbol}", location=location)
		return None

	return url + match["path"] + "#L" + str(match["line"])

class ElixirFunctionRole(SphinxRole):
	def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
		url = get_lxr_url(self.text, self.get_location(), "function")
		
		if url:
			node = nodes.reference(self.rawtext, self.text + "()", refuri=url)
		else:
			node = nodes.Text(self.text + "()")

		return [node], []

class ElixirStructRole(SphinxRole):
	def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
		url = get_lxr_url(self.text, self.get_location(), "struct")
		
		if url:
			node = nodes.reference(self.rawtext, f"struct {self.text}", refuri=url)
		else:
			node = nodes.Text(f"struct {self.text}")

		return [node], []

def setup(app: Sphinx) -> ExtensionMetadata:
	app.add_role('lxr_fn', ElixirFunctionRole())
	app.add_role('lxr_struct', ElixirStructRole())

	return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
