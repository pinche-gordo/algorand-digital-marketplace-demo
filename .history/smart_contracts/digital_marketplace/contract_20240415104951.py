from algopy import *


class DigitalMarketplace(ARC4Contract):
    assetId: UInt64
    unitaryPrice: UInt64

    # create the app
    @arc4.abimethod(allow_actions=["NoOp"], create="require")
    def createApplication(self, assetId: UInt64, unitaryPrice: UInt64) -> None:
        self.assetId = assetId.id
        self.unitaryPrice = unitaryPrice

    # update the listing price
    @arc4.abimethod
    def setPrice(self, unitaryPrice: UInt64) -> None:
        assert Txn.sender == Global.creator_address

        self.unitaryPrice = unitaryPrice

    # opt in to the asset that will be sold
    @arc4.abimethod
    def optInToAsset(self, mbrPay: gtxn.PaymentTransaction) -> None:

        itxn.AssetTransfer(
            xfer_asset=self.assetID,
            asset_receiver=Global.current_application_address,
            asset_amount=0,
        ).submit()

    # but the asset

    # delete the application
