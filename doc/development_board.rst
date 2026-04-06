.. _development_board:

The development board
=====================

`FRDM-IMX93`_ is a small and compact board developed by NXP, which integrates
the `i.MX93`_ chip and offers the following hardware features [#]_:

* 2 x ARM Cortex-A55
* 1 x ARM Cortex-M33
* 3 x USB-C
* 32GB eMMC
* 2GB of RAM
* 40-pin expansion header

A top view of the board is shown in :numref:`frdm-imx93-top-view`.

.. _frdm-imx93-top-view:

.. figure:: _static/figures/FRDM-IMX93-TOP-VIEW.png
   :align: center

   Top view of the FRDM-IMX93 board [#]_

The USB-C ports
---------------

As previously mentioned, the development board is equiped with **three** USB-C
ports, which are highlighted in :numref:`frdm-imx93-usb-c-ports`.

.. _frdm-imx93-usb-c-ports:

.. figure:: _static/figures/FRDM-IMX93-USB-C-PORTS.png
   :align: center

   FRDM-IMX93 USB-C ports

Each of the three USB-C ports serves a different purpose, as described below:

1. **BOOT USB**: used to load the images required during the board's boot process.
2. **POWER USB**: used to supply power to the board.
3. **DEBUG USB**: used for debugging and communicating with the bootloader [#]_.

The boot switch
---------------

Since the board supports multiple boot mediums, users will have to inform the
boot ROM [#]_ where to get the bootloader image from. To do so, the board
provides a series of mechanical switches, which shall be collectively known as the
**boot switch**. Its location is highlighted in :numref:`frdm-imx93-boot-switch`
using yellow.

.. _frdm-imx93-boot-switch:

.. figure:: _static/figures/FRDM-IMX93-BOOT-SWITCH.png
   :align: center

   FRDM-IMX93 boot switch location

The boot switch is made up of **four** switches, numbered from 1 to 4, each having
two possible states: **ON** or **OFF**. The boot medium is selected by placing these
switches into the appropriate states.

The state of the boot switch can be encoded using a group of 4 bits, indexed from 1
to 4 (leftmost being index 1 and rightmost being index 4). Using this encoding, a
value of 0/1 for bit **i** would correspond to switch **i** being OFF/ON. With this
in mind, :numref:`frdm-imx93-boot-mediums` provides the set of supported boot mediums
and the corresponding state of the boot switch.

.. _frdm-imx93-boot-mediums:

.. list-table:: List of supported boot mediums
   :header-rows: 1
   :widths: 30 30
   :align: center

   * - Boot switch state
     - Boot medium

   * - 1000
     - USB

   * - 1100
     - SD

   * - 0100
     - eMMC

For example, if one wishes to boot the board over USB [#]_, according to
:numref:`frdm-imx93-boot-mediums`, one would have to set switch 1 to ON,
switch 2 to OFF, switch 3 to OFF, and switch 4 to OFF.

.. [#] List is not exhaustive.
       For a more comprehensive list of features please check out:
       https://www.nxp.com/design/design-center/development-boards-and-designs/frdm-i-mx-93-development-board:FRDM-IMX93

.. [#] Source: https://www.nxp.com/design/design-center/development-boards-and-designs/FRDM-IMX93

.. [#] Piece of software that gets executed after the boot ROM and is used to load
       the OS (e.g. Linux).

.. [#] Piece of software the automatically gets executed when the board is powered on.

.. [#] This means that the bootloader image is transferred to the board via USB.

.. _i.MX93: https://www.nxp.com/products/processors-and-microcontrollers/arm-processors/i-mx-applications-processors/i-mx-9-processors/i-mx-93-applications-processor-family-arm-cortex-a55-ml-acceleration-power-efficient-mpu:i.MX93

.. _FRDM-IMX93: https://www.nxp.com/design/design-center/development-boards-and-designs/frdm-i-mx-93-development-board:FRDM-IMX93
