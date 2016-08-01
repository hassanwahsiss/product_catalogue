# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import fields, models, exceptions, api, _

class product_catalogue(models.Model):
	
	_name = "product.catalogue"

	withpriceHT = fields.Boolean("Pre-tax price", default=True)
	withpriceTTC = fields.Boolean("Price inc. VAT", default=True)
	withstock = fields.Boolean("With stock", default=True)
	product_ids = fields.Many2many(('product.template'),('product_catalogue_template_rel'),('product_catalogue_id'),
                                    ('template_id'),('Products'))
	name = fields.Char("Catalogue name", size=16, required=True)

