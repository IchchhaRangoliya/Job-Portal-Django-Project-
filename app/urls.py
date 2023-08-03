from django.urls import path,include
from .import views
urlpatterns = [
    path("",views.IndexPage,name="index"), 
    path("signup/",views.SignupPage,name="signup"),
    path("register/",views.RegisterUser,name="register"),
    path("otppage/",views.OTPPage,name="otppage"),
    path("otp/",views.Otpverify,name="otp"),
    path("loginpage",views.Loginpage,name="loginpage"),
    path("loginuser/",views.LoginUser,name="login"),
    path("profile/<int:pk>",views.ProfilePage,name="profile"),
    path("updateprofile/<int:pk>",views.UpdateProfile,name="updateprofile"),
    path("joblist/",views.CandidateJobListPage,name="joblist"),
    path("apply/<int:pk>",views.ApplyPage,name="apply"),
    path("applyjob/<int:pk>",views.ApplyJob,name="applyjob"),

    ###################company side####################

    path("companyindex/",views.CompanyIndexPage,name="companyindex"),
    path("companyprofile/<int:pk>",views.CompanyProfilePage,name="companyprofile"),
    path("updatecompanyprofile/<int:pk>",views.UpdateCompanyProfile,name="updatecompanyprofile"),
    path("jobpostpage",views.JobPostPage,name="jobpostpage"),
    path("jobpost/<int:pk>",views.JobdetailSubmit,name="jobpost"),
    path("jobpostlistpage",views.JobListPage,name="jobpostlistpage"),
    path("companylogout/",views.companylogout,name="companylogout"),
    path("applyjoblist/",views.JobApplyList,name="applylist"),

    ####################Admin Side#########################

    path("adminloginpage/",views.AdminLoginPage,name="adminloginpage"),
    path("adminindex/",views.AdminIndexPage,name="adminindex"),
    path("adminlogin/",views.AdminLogin,name="adminlogin"),
    path("adminuserlist/",views.AdminUserList,name="userlist"),
    path("admincompanylist/",views.AdminCompanyList,name="companylist"),
    path("deleteuser/<int:pk>",views.UserDelete,name="userdelete"),
    path("verifycompanypage/<int:pk>",views.VerifyCompanyPage,name="verifypage"),
    path("verifycompany/<int:pk>",views.VerifyCompany,name="verify"),
    path("deletecompany/<int:pk>",views.CompanyDelete,name="companydelete")
]