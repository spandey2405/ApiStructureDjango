import logging

class PaytmLoggingMixin(object):
    """
    Provides full logging of requests and responses
    """
    def __init__(self):
        self.logger = logging.getLogger('paytm')

    def initial(self, request, *args, **kwargs):
        self.logger = logging.getLogger('paytm')
        try:
            self.logger.debug({"request": request.data})
        except:
            self.logger.debug({"request": dict()})
        super(PaytmLoggingMixin, self).initial(request, *args, **kwargs)

    # def finalize_response(self, request, response, *args, **kwargs):
    #     self.logger = logging.getLogger('paytm')
    #     if response:
    #         self.logger.debug(response.data)
    #     return super(PaytmLoggingMixin, self).finalize_response(request, response, *args, **kwargs)