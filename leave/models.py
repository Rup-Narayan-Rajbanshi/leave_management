# from django.db import models
# from helpers.choices import APPROVAL_CHOICES, LEAVE_CHOICES, PENDING, FULL
# from helpers.models import BaseModel
# from employee.models import CustomUser

# # Create your models here.
# # class FinancialYear(BaseModel):
# #     name = models.CharField(max_length = 20, default = "FY 77/78")
# # 	start_date = models.DateField()
# # 	end_date = models.DateField()

# # 	def __str__(self):
# # 		return self.name


# class Leave(BaseModel):
#     name = models.CharField(max_length=50)
#     no_of_days = models.FloatField()
#     is_active = models.BooleanField(default=False)

#     class Meta:
#         ordering = ["-id"]

#     def __str__(self):
#         return self.name


# class EmployeeLeave(BaseModel):
#     employee = models.ForeignKey(CustomUser, null = True, on_delete = models.CASCADE, related_name="leaves")
#     leave = models.ForeignKey(Leave, null=True, on_delete=models.CASCADE, related_name="leaves")
#     remaining_leave = models.FloatField(null=True, blank=True)
#     can_apply_leave = models.BooleanField(default=True)

#     def __str__(self):
#         return self.employee.first_name

#     class Meta:
#         ordering = ['-id']


# class LeaveRequest(BaseModel):	
#     employee = models.ForeignKey(CustomUser, on_delete=models.PROTECT, null=True, related_name="leave_requests")
#     leave = models.ForeignKey(Leave, on_delete=models.PROTECT, null=True, related_name="leave_requests")
#     leave_type = models.CharField(choices=LEAVE_CHOICES, default=FULL, max_length=15)
#     date_from = models.DateField()
#     date_to = models.DateField()
#     remarks = models.TextField()
#     approval_status = models.CharField(choices=APPROVAL_CHOICES, max_length=15, default=PENDING)

#     class Meta:
#         ordering = ["-id"]

#     def __str__(self):
#         return self.employee.first_name

# 	# def no_of_days(self):
# 	# 	holidays = Holiday.objects.filter(date__gte=self.date_from,date__lte=self.date_to)

# 	# 	# attendance_setting = AttendanceSetting.objects.filter(company=self.request.user.employee.professions.company_department.company).first()

# 	# 	# no_of_days = no_of_days(self.date_to, self.date_from)

# 	# 	# for day in range(no_of_days):
# 	# 	# 	leave_date = self.object.date_from + timedelta(day)
# 	# 	# 	if leave_date.weekday()==attendance_setting.weekoff:
# 	# 	# 		no_of_days = no_of_days - 1

# 	# 	if self.leave_type == LeaveRequest.FULL:
# 	# 		return no_of_days(self.date_to, self.date_from)-len(holidays)
# 	# 	else:
# 	# 		return ((no_of_days(self.date_to, self.date_from)-len(holidays))/2)

# 	# def remaining_days(self):
# 	# 	leave = self.leave
# 	# 	if not leave.no_of_days == None:
# 	# 		allocated_days=leave.no_of_days
# 	# 		days=allocated_days-self.no_of_days()

# 	# 		return days

#     class Meta:
#         ordering = ['-id',]
