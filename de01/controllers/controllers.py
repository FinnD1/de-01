# -*- coding: utf-8 -*-
# from odoo import http


# class De01(http.Controller):
#     @http.route('/de01/de01/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/de01/de01/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('de01.listing', {
#             'root': '/de01/de01',
#             'objects': http.request.env['de01.de01'].search([]),
#         })

#     @http.route('/de01/de01/objects/<model("de01.de01"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('de01.object', {
#             'object': obj
#         })
