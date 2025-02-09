# -*- coding: utf-8 -*-
# from odoo import http


# class ProuductPrice(http.Controller):
#     @http.route('/prouduct_price/prouduct_price', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/prouduct_price/prouduct_price/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('prouduct_price.listing', {
#             'root': '/prouduct_price/prouduct_price',
#             'objects': http.request.env['prouduct_price.prouduct_price'].search([]),
#         })

#     @http.route('/prouduct_price/prouduct_price/objects/<model("prouduct_price.prouduct_price"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('prouduct_price.object', {
#             'object': obj
#         })

