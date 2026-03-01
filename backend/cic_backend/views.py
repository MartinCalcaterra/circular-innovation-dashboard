from django.shortcuts import render, redirect


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")

        if username == "CycleTech":
            return redirect("initial_dashboard")

        elif username == "EcoWrap":
            return redirect("senior_dashboard")

        elif username == "Evergreen":
            return redirect("leader_dashboard")

        elif username == "admin":
            return redirect("admin_dashboard")

    return render(request, "login.html")


def initial_dashboard(request):
    return render(
        request,
        "initial_dashboard.html",
        {
            "company_name": "CycleTech Innovations",
            "engagement": 72,
            "events": 5,
            "cohort_name": "Cohort 2025",
            "role": "initial",
        },
    )


def senior_dashboard(request):
    return render(
        request,
        "senior_dashboard.html",
        {
            "company_name": "EcoWrap Industries",
            "engagement": 88,
            "events": 12,
            "cohort_name": "Cohort 2025",
            "role": "senior",
        },
    )


def leader_dashboard(request):
    return render(
        request,
        "leader_dashboard.html",
        {
            "company_name": "Evergreen Manufacturing",
            "engagement": 95,
            "events": 20,
            "cohort_name": "Cohort 2025",
            "role": "leader",
        },
    )


def admin_dashboard(request):
    return render(request, "admin_dashboard.html")
