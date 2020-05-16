# -*- coding: utf-8 -*-
# from odoo import http


# class CallCenter2(http.Controller):
#     @http.route('/call_center_2/call_center_2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/call_center_2/call_center_2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('call_center_2.listing', {
#             'root': '/call_center_2/call_center_2',
#             'objects': http.request.env['call_center_2.call_center_2'].search([]),
#         })

#     @http.route('/call_center_2/call_center_2/objects/<model("call_center_2.call_center_2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('call_center_2.object', {
#             'object': obj
#         })
