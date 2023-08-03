from django.shortcuts import render,redirect
from .models import *
from random import randint
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.

def IndexPage(request):
    return render(request,"app/index.html")

def SignupPage(request):
    return render(request,"app/signup.html")

def RegisterUser(request):
    if request.POST.get('role')=="Candidate":
        role = request.POST.get('role')
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User already exist"
            return render(request,"app/signup.html",{'msg':message})
        else:
            if password == cpassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcand = Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                return render(request,"app/otpverify.html",{'email':email})
    else:
        if request.POST.get('role')=="Company":
            role = request.POST.get('role')
            fname = request.POST.get('firstname')
            lname = request.POST.get('lastname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')

            user = UserMaster.objects.filter(email=email)

            if user:
                message = "Company already exist"
                return render(request,"app/signup.html",{'msg':message})
            else:
                if password == cpassword:
                    otp = randint(100000,999999)
                    newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                    newcompany = Company.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                    return render(request,"app/otpverify.html",{'email':email})

def OTPPage(request):
    return render(request,"app/otpverify.html")


def Otpverify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])
    
    user=UserMaster.objects.get(email=email)
    if user:
        if user.otp == otp:
            message = "Otp verify successfully"
            return render(request,"app/login.html",{'msg':message})
        else:
            message = "Otp is incorrect"
            return render(request,"app/otpverify.html",{'msg':message})
    else:
        return render(request,"app/signup.html")
    


def Loginpage(request):
    return render(request,"app/login.html")

def LoginUser(request):
    if request.POST['role']=="Candidate":
        email = request.POST['email']
        password = request.POST['password']

        user =UserMaster.objects.get(email=email)
        

        if user:
            if user.password == password and user.role =="Candidate":
                can = Candidate.objects.get(user_id=user)
                request.session['id']=user.id 
                request.session['role']=user.role 
                request.session['firstname']=can.firstname
                request.session['lastname']=can.lastname
                request.session['email']=user.email
                return redirect('index')
            else:
                message = "Password doesnot Match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message ="User doesnot exist"
            return render(request,"app/login.html",{'msg':message})
        
    elif request.POST['role']=="Company":
        email = request.POST['email']
        password = request.POST['password']

        user = UserMaster.objects.get(email=email)

        if user:
            if user.password == password and user.role =="Company":
                company = Company.objects.get(user_id=user)
                request.session['id']=user.id 
                request.session['role']=user.role
                request.session['firstname']=company.firstname
                request.session['lastname']=company.lastname
                request.session['email']=user.email
                request.session['password']=user.password
                return redirect('companyindex')
            else:
                message = "Password doesnot Match"
                return render(request,"app/login.html",{'msg': message})
        else:
            message = "User doesnot Exist"
            return render(request,"app/login.html",{'msg':message})  


def ProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    can = Candidate.objects.get(user_id=user)
    return render(request,"app/profile.html",{'user':user,'can':can})


def UpdateProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id=user)
        can.state =request.POST['state']
        can.city = request.POST['city']
        can.job_type = request.POST['jobtype']
        can.jobcategory = request.POST['category']
        can.highestedu = request.POST['education']
        can.experience = request.POST['experience']
        can.website = request.POST['website']
        can.shift = request.POST['shift']
        can.jobdescription = request.POST['description']
        can.min_salary = request.POST['min_salary']
        can.max_salary = request.POST['max_salary']
        can.contact = request.POST['contact']
        can.gender = request.POST['gender']
        can.profile_pic = request.FILES['image']
        can.save()
        url = f'/profile/{pk}'   #formatting URL  (jab apke kisi view k response ko ksi durse view ki value me pass krni hai aur usme koi id ya argument pass ho rahi hai to formatting url ka use krte hai.)
        return redirect(url)
    

def ApplyPage(request,pk):
    user = request.session['id']
    if user:
        can = Candidate.objects.get(user_id=user)
        job = JobDetails.objects.get(id=pk)
    return render(request,"app/apply.html",{'user':user,'can':can,'job':job})

def ApplyJob(request,pk):
    user = request.session['id']
    if user:
        can = Candidate.objects.get(user_id=user)
        job = JobDetails.objects.get(id=pk)
        edu = request.POST['education']
        exp = request.POST['experience']
        web = request.POST['website']
        gender = request.POST['gender']
        resume = request.FILES['resume']
        min_salary = request.POST['min_salary']
        max_salary = request.POST['max_salary']
        newapply = ApplyList.objects.create(Candidate=can,job=job,education=edu,website=web,min_salary=min_salary,
                                           max_salary=max_salary,gender=gender,resume=resume)
        message = "Applied Succefully"
        return render(request,"app/apply.html",{'msg':message})

#############################company side#########################

def CompanyIndexPage(request):
    return render(request,"app/company/index.html")

def CompanyProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    company = Company.objects.get(user_id=user)
    return render(request,"app/company/company_profile.html",{'user':user,'company':company})

def UpdateCompanyProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Company":
        company = Company.objects.get(user_id=user)
        company.firstname =request.POST['firstname']
        company.lastname =request.POST['lastname']
        company.state =request.POST['state']
        company.city = request.POST['city']
        company.company_name = request.POST['companyname']
        company.website = request.POST['website']
        company.companydescription = request.POST['description']
        company.address = request.POST['address']
        company.contact = request.POST['contact']
        company.logo_pic = request.FILES['image']
        company.save()
        url = f'/companyprofile/{pk}'   #formatting URL  (jab apke kisi view k response ko ksi durse view ki value me pass krni hai aur usme koi id ya argument pass ho rahi hai to formatting url ka use krte hai.)
        return redirect(url)
    

def JobPostPage(request):
    return render(request,"app/company/jobpost.html")

def JobdetailSubmit(request,pk):
    user = UserMaster.objects.get(pk=pk)
    
    if user.role == "Company":
        company = Company.objects.get(user_id=user)
        jobname = request.POST['jobname']
        companyname = request.POST['companyname']
        address = request.POST['companyaddress']
        companyemail = request.POST['companyemail']
        companycontact = request.POST['companycontact']
        jobdescription = request.POST['jobdescription']
        qualification = request.POST['qualification']
        responsibilities = request.POST['responsibilities']
        location = request.POST['location']
        salary = request.POST['salary']
        experience = request.POST['experience']
        website = request.POST['website']
        logo = request.FILES['image']

        newjob = JobDetails.objects.create(company_id=company,jobname=jobname,companyname=companyname,companyaddress=address,qualification=qualification,responsibilities=responsibilities,location=location,
                                           companywebsite=website,companyemail=companyemail,companycontact=companycontact,salarypackage=salary,jobdescription=jobdescription,experience=experience,logo=logo)
        
        message = "Job Post SuccessFully"
        return render(request,"app/company/jobpost.html",{'msg':message})
    

def JobListPage(request):
    all_job = JobDetails.objects.all()
    return render(request,"app/company/jobpostlist.html",{'all_job':all_job})

def CandidateJobListPage(request):
    all_job = JobDetails.objects.all()
    return render(request,"app/job-list.html",{'all_job':all_job})

def JobApplyList(request):
    all_job_apply = ApplyList.objects.all()
    return render(request,"app/company/applyjoblist.html",{'all_job':all_job_apply})

def companylogout(request):
    del request.session["email"]
    del request.session["password"]
    return redirect("index")

################################# Admin Side #############################


def AdminLoginPage(request):
    return render(request,"app/admin/login.html")

def AdminIndexPage(request):
    if 'username' in request.session and 'password' in request.session:
        return render(request,"app/admin/index.html")
    else:
        return redirect('adminloginpage')

def AdminLogin(request):
    username = request.POST['username']
    password = request.POST['password']

    if username == "admin" and password == "admin":
        request.session['username'] = username
        request.session['password'] = password
        return redirect('adminindex')
    else:
        message = "Username And Password not Match"
        return render(request,"app/admin/login.html",{'msg':message})
    

def AdminUserList(request):
    all_user = UserMaster.objects.filter(role="Candidate")
    return render(request,"app/admin/userlist.html",{'alluser':all_user})

def AdminCompanyList(request):
    all_company = UserMaster.objects.filter(role="Company")
    return render(request,"app/admin/companylist.html",{'allcompany':all_company})

def UserDelete(request,pk):
    user = UserMaster.objects.get(pk=pk)
    user.delete()
    return redirect('userlist')

def VerifyCompanyPage(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        return render(request,"app/admin/verify.html",{'company':company})
    
def VerifyCompany(request,pk):
    company = UserMaster.objects.get(pk=pk)
    if company:
        company.is_verified = request.POST['verify']
        company.save()
        return redirect('companylist')
    

def CompanyDelete(request,pk):
    company = UserMaster.objects.get(pk=pk)
    company.delete()
    return redirect('companylist')
    