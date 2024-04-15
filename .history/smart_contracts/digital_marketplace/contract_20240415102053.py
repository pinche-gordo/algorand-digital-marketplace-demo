from algopy import *


class DigitalMarketplace(ARC4Contract):
    assetId: UInt64
    unitaryPrice: UInt64

    # create the app
    @arc4.abimethod(allow_actions=["NoOp"], create="require")
    def createApplication(self, assetId: Asset, unitaryPrice: UInt64) -> None:
        self.assetId = assetId
        self.unitaryPrice = unitaryPrice

    # update the listing price

    # opt in to the asset that will be sold

    # but the asset

    # delete the application
