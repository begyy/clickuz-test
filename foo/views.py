from clickuz.views import ClickUzMerchantAPIView
from clickuz import ClickUz


class CheckOrderAndPayment(ClickUz):

    def check_order(self, order_id: str, amount: str):
        if order_id == '1' and amount == '500':
            return self.ORDER_FOUND
        if order_id == '1' and amount != '500':
            return self.INVALID_AMOUNT
        return self.ORDER_NOT_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        if order_id != '1':
            raise ValueError


class ClickView(ClickUzMerchantAPIView):
    VALIDATE_CLASS = CheckOrderAndPayment
