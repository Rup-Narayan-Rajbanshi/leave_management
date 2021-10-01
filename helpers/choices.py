from .constants import LEAVE_TYPE, APPROVAL_TYPE

APPROVAL_CHOICES = (
	(APPROVAL_TYPE['PENDING'], "Pending"),
	(APPROVAL_TYPE['YES'], "Approved"),
	(APPROVAL_TYPE['NO'],"Not Approved")
)


LEAVE_CHOICES = (
	(LEAVE_TYPE['FULL'],'Full'),
	(LEAVE_TYPE['HALF'],'Half'),
)