from django.shortcuts import render, redirect


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")

        if username == "smallcompany":
            return redirect("/user/?company=smallcompany")

        elif username == "bigcompany":
            return redirect("/user/?company=bigcompany")

        elif username == "admin":
            return redirect("/admin/")

    return render(request, "login.html")


def user_dashboard(request):
    company = request.GET.get("company", "smallcompany")

    if company == "smallcompany":
        context = {
            "tier": "Small Business",
            "engagement": 62,
            "cohort": "Scaling & Capability Cohort",
            "mentor_button": "Request Mentor",
        }

    else:
        context = {
            "tier": "Industry Leadership",
            "engagement": 88,
            "cohort": "Policy & Strategic Leadership Cohort",
            "mentor_button": "Become a Mentor",
        }

    return render(request, "user_dashboard.html", context)


def admin_dashboard(request):
    companies = [
        {"name": "smallcompany", "tier": "Small Business", "engagement": 62},
        {"name": "bigcompany", "tier": "Industry Leadership", "engagement": 88},
    ]

    return render(request, "admin_dashboard.html", {"companies": companies})
