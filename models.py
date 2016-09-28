from openerp import models, fields, api, _
from openerp.osv import osv
from openerp.exceptions import except_orm, ValidationError
from StringIO import StringIO
import urllib2, httplib, urlparse, gzip, requests, json
import openerp.addons.decimal_precision as dp
import logging
import datetime
from openerp.fields import Date as newdate

#Get the logger
_logger = logging.getLogger(__name__)

class res_partner(models.Model):
	_inherit = 'res.partner'

	@api.one
	@api.constrains('function')
	def _check_partner_function(self):
		if not self.is_company and (self.customer or self.supplier):
			if not self.function:
			        raise ValidationError("Function is mandatory in contacts")


	@api.one
	@api.constrains('email')
	def _check_partner_function(self):
		if not self.function:
		        raise ValidationError("Email is mandatory in partners")


