from django.shortcuts import render
from .models import Staff, Role 


def students(request):
    return render(request, 'students/students.html')
def studentrules(request):
    file = [
    {
      'url': '/static/pdf/announcement/2023/12/Students_General_Rules_updated 18_20.pdf',
      'filename': 'Institute Rules and Regulations'
    }
    ]
    return render(request, 'students/studentrules.html',{'file': file})
def anti_ragging(request):  
    file = [
    {
      'filename':"UGC Regulation on Curbing the Menace of Ragging in Higher Educational Institutions, 2009",
      'url':'/static/docs/studentwelfare/Anti-Ragging/UGC Regulation on Curbing the Menace of Ragging in Higher Educational Institutions, 2009.pdf',
    },
    {
      'filename':'UGC Regulation on Curbing the Menace of Ragging in Higher Educational Institutions (First Amendment), 2012',
      'url':'/static/docs/studentwelfare/Anti-Ragging/UGC Regulation on Curbing the Menace of Ragging in Higher Educational Institutions (First Amen.pdf'
    },
    {
      'filename':'UGC Regulation on Curbing the Menace of Ragging in Higher Educational Institutions (Second Amendment), 2013',
      'url':'/static/docs/studentwelfare/Anti-Ragging/UGC Regulation on Curbing the Menace of Ragging in Higher Educational Institutions (Second Ame.pdf'
    },
    {
      'filename':'UGC Regulation on Curbing the Menace of Ragging in Higher Educational Institutions (Third Amendment), 2016',
      'url':'/static/docs/studentwelfare/Anti-Ragging/UGC Regulation on Curbing the Menace of Ragging in Higher Educational Institutions (Third Amen.pdf'
    },
    {
      'filename':'Undertaking from the Parent as per the provisions of anti-ragging verdict by the Hon’ble Supreme Court (affidavit by parent_guardian)',
      'url':'/static/docs/studentwelfare/Anti-Ragging/Undertaking from the Parent as per the provisions of anti-ragging verdict by the Honble Supreme Court (affidavit by parent_guardian).pdf'
    },
    {
      'filename':'Undertaking from the Students as per the provisions of anti-ragging verdict by the Hon’ble Supreme Court (affidavit by the student)',
      'url':'/static/docs/studentwelfare/Anti-Ragging/Undertaking from the Students as per the provisions of anti-ragging verdict by the Honble Supreme Court (affidavit by the student).pdf'
    },
    {
      'filename':'Anti-ragging poster',
      'url':'/static/docs/studentwelfare/Anti-Ragging/Anti-ragging poster.pdf'
    },
    {
      'filename':'Anti Ragging Cell Circular_2023_UGC',
      'url':'/static/docs/studentwelfare/Anti-Ragging/Anti-Ragging_Cell_Circular.pdf'
    },
    {
      'filename':'Information education communication (IEC) guidelines for councils, universities & colleges_curbing the menace of ragging',
      'url':'/static/docs/studentwelfare/Anti-Ragging/ugc-iec-guidlines-for-councils-universities-and-colleges-for-curbing-the-menace-of-ragging.pdf'
    },
    ]
    files = [
    {
      'url': '/static/docs/studentwelfare/Anti-Ragging/AntiRagging report.pdf',
      'filename': 'Anti-Ragging Awareness Report.pdf'
    }
    ]
    return render(request, 'students/anti_ragging.html',{'file': file,'files': files})
def annualfest(request):    
    
    leciel=[
    {
        'title':"Leciel 2024-25",
        'url':'/static/docs/studentwelfare/leciel report/leciel report 2024-25.pdf',
    },
    ]
    return render(request, 'students/annualfest.html',{'leciel':leciel})
def orientation(request):
    orientation = [
    {
      'pic': "images/events/orientation program 01 2024.jpg",
      'name': ""
    },
    {
      'pic': "images/events/orientation program 02 2024.jpg",
      'name': ""
    },
    ]
    return render(request, 'students/orientation.html',{'orientation':orientation})
def clubs(request):
    clubCategories = [
        {
            'category': 'Technical Clubs',
            'clubs': [
                  { 'name': 'Design Club', 'facultyInCharge'  : ['Dr. Vani V AP CSE', 'Dr. Revathi S AP EEE'] },
                  { 'name': 'Esports Club', 'facultyInCharge': ['Dr. Narendran Rajagopalan Asso. Prof CSE'] },
                  { 'name': 'Coding Club', 'facultyInCharge': ['Dr. Kumaran P AP CSE', 'Dr. Karthik N AP CSE'] },
                  { 'name': 'FOSS Club', 'facultyInCharge': ['Dr. Narendran Rajagopalan Asso. Prof CSE'] },
                  { 'name': 'Robotics Club', 'facultyInCharge': ['Dr. M. V. A. Raju Bahubalendruni AP ME'] },
                  { 'name': 'ANTRiX Club', 'facultyInCharge': ['Dr. Amrtha Bhide Asso. Prof Physics'] },
                  { 'name': 'BIS Standards Club', 'facultyInCharge': ['Dr. J. Ronald Aseer AP ME'] }

            ]
        },
        {
            'category': 'Cultural Clubs',
            'clubs':[
                {"name": "Photography Club", "facultyInCharge": ["Dr. Ansuman Mahapatra AP CSE", "Dr. Sunanda Ambulkar AP CSE"]},
                {"name": "Videography Club", "facultyInCharge": ["Dr. Ansuman Mahapatra AP CSE"]},
                {"name": "Ragasvarupam Indian Performing Arts (RIPA) Club", "facultyInCharge": ["Dr. A. Venkadesan Asso. Prof EEE"]},
                {"name": "Dance Club", "facultyInCharge": ["Dr. Sanjay Bankapur AP CSE", "Dr. Nidhi M Civil Engg"]},
                {"name": "Music Club", "facultyInCharge": ["Dr. S. Babu SASO"]},
                {"name": "Arts and Crafts Club", "facultyInCharge": ["Dr. Gautham A AP Civil Engg", "Dr. Lalrinpuia Tlau AP Mathematics"]},
                {"name": "Culturehood - Fashion Club", "facultyInCharge": ["Dr. Nidhi M AP CE"]},
                {"name": "Literary Club", "facultyInCharge": ["Dr. Smrutisikta Mishra Asso. Prof Humanities and Social Sciences"]},
                {"name": "Year Book Club", "facultyInCharge": ["Dr. Thomas Joseph AP ECE"]},
                {"name": "Language Club", "facultyInCharge": ["Dr. Ajay Kumar Mishra AP Physics (Hindi)", "Dr Aniruddha Kanhe AP ECE(Hindi)", "Dr. Karpagaraj A AP ME (Tamil)", "Dr. Naveen Raj R AP ME (Tamil)", "Dr. Hemachander A AP EEE (Telugu)", "Dr. Nidhi M AP CE (Malayalam)"]},
            ],
        },
        {
            "category": "Social Clubs",
            "clubs": [
                {"name": "Finance Club", "facultyInCharge": ["Dr. Thomas Joseph AP ECE"]},
                {"name": "Propel & Progress Society", "facultyInCharge": ["Dr.Perumalla Venkata Mallikarjun Rao AP CE"]},
                {"name": "UPSC Civil Services Club", "facultyInCharge": ["Dr Aniruddha Kanhe AP ECE"]},
            ],
        },
    ]
    return render(request, 'students/clubs.html',{'clubCategories': clubCategories})
def student_association(request):
    associations = [
        {
            "department": "Civil Engineering",
            "association_name": "Civil Engineering Association (CEA)",
            "faculty_in_charge": ["Dr. Nidhi M", "Dr. Gautham A"],
        },
        {
            "department": "Computer Science and Engineering",
            "association_name": "Association of Computer Science Engineers (ACE)",
            "faculty_in_charge": ["Dr. Narendran Rajagopalan"],
        },
        {
            "department": "Electrical and Electronics Engineering",
            "association_name": "Society of Powerful and Realistic Electrical Engineers (SPREE)",
            "faculty_in_charge": ["Dr. Bijukumar B"],
        },
        {
            "department": "Electronics and Communication Engineering",
            "association_name": "ECE Student Association",
            "faculty_in_charge": ["Dr. Thomash Joseph"],
        },
        {
            "department": "Electronics and Communication Engineering",
            "association_name": "IEI Student Chapter",
            "faculty_in_charge": ["Dr. Sunada Ambulker"],
        },
        {
            "department": "Mathematics",
            "association_name": "Delta Mathematics Association",
            "faculty_in_charge": ["Dr. Lalrinpuia Tlau"],
        },
        {
            "department": "Mechanical Engineering",
            "association_name": "Mechanical Engineering Association (MEA)",
            "faculty_in_charge": ["Dr. Vadivukkarasan M", "Dr. Jack.J.Kenned"],
        },
        {
            "department": "Mechanical Engineering",
            "association_name": "Society of Automotive Engineers (SAE)",
            "faculty_in_charge": ["Dr. Karpagaraj. A", "Dr. SathishKumar . P"],
        },
    ]
    return render(request, 'students/student_association.html', {'associations': associations})
def counselling_service(request):
    return render(request, 'students/counselling_services.html')
def grievance_redressal(request):
    return render(request, 'students/grievance_redressal.html')

def sw_announcements(request):
     announcement24_25=[
    {
      'title':'The Election for the General Body of the Student Council for the AY 2024-2025 is scheduled on 25-07-2024',
      'url':''
    }
  ]
     return render(request, 'students/sw_announcements.html',{'announcement24_25':announcement24_25})
def medical_insurance(request):
    file = [
    
    {
      'filename':"Medi Assist - Reimbursement Claim Form",
      'url':'/static/docs/studentwelfare/mediclaim/2024-2025/Medi Assist - Reimbursement Claim Form.pdf',

    },
    {
      'filename':"Medi Assist - NOC format",
      'url':'/static/docs/studentwelfare/mediclaim/2024-2025/Medi Assist - NOC format.PDF',

    },
    {
      'filename':"Policy Schedule - Students Safety Package Insurance",
      'url':'/static/docs/studentwelfare/mediclaim/2024-2025/Policy Schedule - Students Safety Package Insurance.pdf',

    },
    {
      'filename':"Policy Schedule - Group Mediclaim Policy",
      'url':'/static/docs/studentwelfare/mediclaim/2024-2025/Policy Schedule - Group Mediclaim Policy.pdf',

    },
    {
      'filename':"Terms, Conditions and Procedures",
      'url':'/static/docs/studentwelfare/mediclaim/2024-2025/Terms, Conditions and Procedures.pdf',

    },

    ]
    return render(request, 'students/medical_insurance.html',{'file': file})

def studentActivities(request):
    return render(request, 'students/studentActivities.html')

def aluminiRelations(request):
    main_link = {
        'title': 'Administration',
        'link': '/institute/administration'
    }

    links = [
        {'title': 'Visitor', 'link': 'visitor'},
        {'title': 'Chairman', 'link': 'chairman'},
        {'title': 'Director', 'link': 'director'},
        {'title': 'Board of Governors', 'link': 'board-of-governors'},
        {'title': 'Senate', 'link': 'senate'},
        {'title': 'Registrar', 'link': 'registrar'},
        {'title': 'Vigilance Officer', 'link': 'vigilance-officer'},
        {'title': 'Deans', 'link': 'deans'},
        {'title': 'Associate Deans', 'link': 'associate-deans'},
        {'title': 'Nodal Officers and Co-ordinators', 'link': 'nodal-officers'},
        {'title': 'Heads of Departments', 'link': 'hods'},
    ]
    return render(request, "students/aluminiRelations.html", {
        'mainLink': main_link,
        'links': links
    })

def internship(request):
    
    details = [
    {
        "dept": "CIVIL",
        "internship": "A VBA-Based Application for Efficient Steel Structure Design",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "CIVIL",
        "internship": "Assessment of Wind-Induced Damage to Critical Infrastructure",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "CIVIL",
        "internship": "Machine Learning for Concrete Strength Prediction",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "CIVIL",
        "internship": "Non-Linear Analysis of Prestressed Concrete Members",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "CIVIL",
        "internship": "Movement of Microplastics in River Bed",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "CIVIL",
        "internship": "Prediction of Coastline Erosion using AI",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "CSE",
        "internship": "Computer Vision",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "CSE",
        "internship": "Internet of Things",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "CSE",
        "internship": "Cloud and Fog computing",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mathematics",
        "internship": "Differential Equations and Their Applications",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mathematics",
        "internship": "Mathematical Biology",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "Augmented Reality for Manufacturing applications",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "E-waste Management for Co2 release rate and Circular Economy",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "Human robot collaboration",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "Lattice Structures for specific energy absorption and blast resistance",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "Auxetic materials for biomedical applications",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "Damage Identification and localization based on vibration signals",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "Computer vision techniques to find vibration measurements from videos",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "Thermal Imaging",
        "duration": "Summer Vacation (2 months)",
    },
    {
        "dept": "Mechanical",
        "internship": "Computational Fluid Dynamics",
        "duration": "Summer Vacation (2 months)",
    },
]


    return render(request, "students/internship.html", {"details": details})

def welfare(request):
    associate_deans = [
        {
            'name': 'Dr. Balakumar V',
            'responsibilities': [
                'Student Council elections',
                'Annual Fests',
                'Orientation',
                'Student Clubs',
                'Student Associations',
                'Medical Insurance',
                'NCC',
                'Sports',
                'Alumni relations',
                'Grievance Redressal',
                'Institute Discipline'
            ]
        },
        {
            'name': 'Dr. Vani V',
            'responsibilities': [
                'Anti-ragging',
                'Student Council elections',
                'Annual Fests',
                'Orientation',
                'Student Clubs',
                'Student Association',
                'Counselling Services',
                'NSS',
                'Grievance Redressal',
                'Campus Connect',
                'Girls mentoring'
            ]
        }
    ]
    # Get staff with training and placement role
    welfare_roles = Role.objects.filter(role__icontains="Welfare")

    associate_dean_roles = welfare_roles.filter(role__icontains="Associate Dean").select_related('id')

    dean_roles = welfare_roles.filter(role__icontains="Dean").exclude(role__icontains="Associate Dean").select_related('id')
    
    # Get unique staff members from those roles
    dean_ids = dean_roles.values_list('id', flat=True).distinct()
    dean_list = Staff.objects.filter(id__in=dean_ids)
    
    associate_dean_ids = associate_dean_roles.values_list('id', flat=True).distinct()
    associate_dean_list = Staff.objects.filter(id__in=associate_dean_ids)

    # Get the relevant role for each staff (for display)
    dean_roles = {role.id_id: role for role in dean_roles}
    associate_dean_roles = {role.id_id: role for role in associate_dean_roles}

    context = {
        'dean_list': dean_list,
        'dean_roles': dean_roles,
        'associate_dean_list': associate_dean_list,
        'associate_dean_roles': associate_dean_roles,
        'associate_deans': associate_deans
    }
    return render(request, 'students/welfare.html',context)

def council(request):
    # Table data for council members
    council_data = [
        {
            "post": "President",
            "name": "Asif Rijo",
            "roll": "ME21B1030",
            "mobile": "99955 76275"
        },
        {
            "post": "Vice-President",
            "name": "Mohana G",
            "roll": "EE21B1030",
            "mobile": "63741 18839"
        },
        {
            "post": "General Secretary",
            "name": "Thinnavalli Sree",
            "roll": "CS22B1057",
            "mobile": "90329 99819"
        },
        {
            "post": "Joint Secretary - I",
            "name": "Ramajayam D",
            "roll": "ME21D1006",
            "mobile": "97511 10694"
        },
        {
            "post": "Joint Secretary - II",
            "name": "Bitla Mukesh Chandra",
            "roll": "EE23B1011",
            "mobile": "85198 51921"
        },
        {
            "post": "Joint Secretary - III",
            "name": "Kowshik V",
            "roll": "CH23M1006",
            "mobile": "82486 06657"
        },
        {
            "post": "Joint Secretary - IV",
            "name": "G Hemasiva Sankari",
            "roll": "ED23B1014",
            "mobile": "70107 74835"
        },
    ]

    welfare_roles = Role.objects.filter(role__icontains="Welfare").select_related('id')
    
    # Get unique staff members from those roles
    staff_ids = welfare_roles.values_list('id', flat=True).distinct()
    staff_list = Staff.objects.filter(id__in=staff_ids)

    # Get the relevant role for each staff (for display)
    staff_roles = {role.id_id: role for role in welfare_roles}

    context = {
        'staff_list': staff_list,
        'staff_roles': staff_roles,
        "council_data": council_data,
    }
    return render(request, 'students/council.html',context)


def ncc(request):
    staff_list = Staff.objects.filter(
        designation__iexact="Senior SASO",
        department__iexact="Physical Education"
    ).prefetch_related('role_set')

    context = {
        'staff_list': staff_list,
    }
    return render(request, 'students/ncc.html', context)


def nss(request):  
    nss2025 = [
        {
            'title': '1. Mera Vote Campaign Report',
            'url': '/static/docs/NSS Report/NSS Report/2024-2025/1. Mera-Vote-Campaign-Report-NITPY.pdf'
        },
        {
            'title': '2. International Consumer Day Report',
            'url': '/static/docs/NSS Report/NSS Report/2024-2025/2. International-Consumer-Day-Report.pdf'
        },
        {
            'title': '3. Red Run Report 09-08-2024',
            'url': '/static/docs/NSS Report/NSS Report/2024-2025/3. Red Run Report 09-08-2024.pdf'
        },
        {
            'title': '4. HIV awareness program report 19-09-24',
            'url': '/static/docs/NSS Report/NSS Report/2024-2025/4. HIV awareness program report 19-09-24.pdf'
        },
        {
            'title': '5. Coastal clean up report 21-09-24',
            'url': '/static/docs/NSS Report/NSS Report/2024-2025/5. Coastal clean up report 21-09-24.pdf'
        },
        {
            'title': '6. Cleanliness Drive Report 17-09-2024',
            'url': '/static/docs/NSS Report/NSS Report/2024-2025/6. Cleanliness Drive Report 17-09-2024 to 02-10-2024.pdf'
        },
        {
            'title': '7. Drawing and speech competition on tobacco awareness 15-10-2024',
            'url': '/static/docs/NSS Report/NSS Report/2024-2025/7. Drawing and speech competition on tobacco awareness 15-10-2024.pdf'
        },
        {
            'title': '8. Tobacco awareness Report 16-10-2024',
            'url': '/static/docs/NSS Report/NSS Report/2024-2025/8. Tobacco awareness Report 16-10-2024.pdf'
        },
        {
            'title': '9. Cleanliness program under special campaign 4.0 to improve institute swachhata',
            'url': '/static/docs/NSS Report/NSS Report/2024-2025/9. Cleanliness program under special campaign 4.0 to improve institute swachhata.pdf'
        },
        {
            'title': '10. Awareness Programme on Drug Abuse – Report',
            'url': '/static/docs/NSS Report/NSS Report/2024-2025/10. Awareness Programme on Drug Abuse – Report.pdf'
        },
        {
            'title': '11. Constitution Day Celebration',
            'url': '/static/docs/NSS Report/NSS Report/2024-2025/11. Constitution Day Celebration.pdf'
        },
        {
            'title': "12.Celebration of National Voter's Day",
            'url': "/static/docs/NSS Report/NSS Report/2024-2025/12.Celebration of National Voter's Day.pdf"
        },
        {
            'title': "13.Good Governance Week Report",
            'url': "/static/docs/NSS Report/NSS Report/2024-2025/13.Good governance week_report.pdf"
        },
    ]

    nss2024 = [
        {
            'title': 'Chandrayaan-3 Maha Quiz',
            'url': '/static/docs/NSS Report/NSS Report/2024/Chandrayaan-3 Maha Quiz.pdf'
        },
        {
            'title': 'National Unity Day Report',
            'url': '/static/docs/NSS Report/NSS Report/2024/National Unity Day Report.pdf'
        },
        {
            'title': 'Drama-Skit Competition Report',
            'url': '/static/docs/NSS Report/NSS Report/2024/Drama-Skit Competition Report.pdf'
        },
        {
            'title': 'Swachhata Hi Seva Report',
            'url': '/static/docs/NSS Report/NSS Report/2024/Swachhata hi seva report.pdf'
        },
        {
            'title': 'LEAP (Learn Educate And Prosper) Inaguration Report',
            'url': '/static/docs/NSS Report/NSS Report/2024/LEAP inaguration report.pdf'
        },
        {
            'title': 'Coastal Cleanup Report',
            'url': '/static/docs/NSS Report/NSS Report/2024/Coastal Cleanup Report.pdf'
        },
        {
            'title': 'Painting Competition Report',
            'url': '/static/docs/NSS Report/NSS Report/2024/Painting Competition Report.pdf'
        },
        {
            'title': 'Red Run Competition',
            'url': '/static/docs/NSS Report/NSS Report/2024/Report of Red Run Competition 2023.pdf'
        },
        {
            'title': 'Distribution of National Flag',
            'url': '/static/docs/NSS Report/NSS Report/2024/Distribution of National Flag.pdf'
        },
        {
            'title': 'Indian Organ Donation Day',
            'url': '/static/docs/NSS Report/NSS Report/2024/NIT Puducherry - Indian Organ Donation Day - Pledge - Report.pdf'
        },
    ]
    nss2023 = [
        {'title': '1-Participation in National Voters Day Competition', 'url': '/static/docs/NSS Report/NSS Report/2023/1-Participation in National Voters Day Competition.pdf'},
        {'title': '2-Pledge-National Voters Day', 'url': '/static/docs/NSS Report/NSS Report/2023/2-Pledge-National Voters Day.pdf'},
        {'title': '3-Blood Donation Camp at GH', 'url': '/static/docs/NSS Report/NSS Report/2023/3-Blood Donation Camp at GH.pdf'},
        {'title': '4-Training on Basic Life Support', 'url': '/static/docs/NSS Report/NSS Report/2023/4-Training on Basic Life Support.pdf'},
        {'title': '5-Tree Plantation Drive', 'url': '/static/docs/NSS Report/NSS Report/2023/5-Tree Plantation Drive.pdf'},
        {'title': '6-Pledge against Drug Abuse', 'url': '/static/docs/NSS Report/NSS Report/2023/6-Pledge against Drug Abuse.pdf'},
        {'title': '7-Service at Institute Vaccine Camp', 'url': '/static/docs/NSS Report/NSS Report/2023/7-Service at Institute Vaccine Camp.pdf'},
        {'title': '8-Pledge-Clean Coast Safe Sea', 'url': '/static/docs/NSS Report/NSS Report/2023/8-Pledge-Clean Coast Safe Sea.pdf'},
        {'title': '9-Seminar on Potential of Millets', 'url': '/static/docs/NSS Report/NSS Report/2023/9-Seminar on Potential of Millets.pdf'},
        {'title': '10-Regional Pollution Response Exercise', 'url': '/static/docs/NSS Report/NSS Report/2023/10-Regional Pollution Response Exercise.pdf'},
        {'title': '11-Rally and Sapling Plantation', 'url': '/static/docs/NSS Report/NSS Report/2023/11-Rally and Sapling Plantation.pdf'},
        {'title': '12-Single use Plastic Awareness and Cleaning Activity', 'url': '/static/docs/NSS Report/NSS Report/2023/12-Single use Plastic Awareness and Cleaning Activity.pdf'},
        {'title': '13-NIFTEM Visit', 'url': '/static/docs/NSS Report/NSS Report/2023/13-NIFTEM Visit.pdf'},
        {'title': '14-Coastal Clean-up event at Mandapathur Village', 'url': '/static/docs/NSS Report/NSS Report/2023/14-Coastal Clean-up event at Mandapathur Village.pdf'},
        {'title': '15-International Sign Language Day', 'url': '/static/docs/NSS Report/NSS Report/2023/15-International Sign Language Day.pdf'},
        {'title': '16-LEAP Inauguration', 'url': '/static/docs/NSS Report/NSS Report/2023/16-LEAP Inauguration.pdf'},
        {'title': '17-New Voter Registration  Drive', 'url': '/static/docs/NSS Report/NSS Report/2023/17-New Voter Registration  Drive.pdf'},
        {'title': '18-Clean Campus Activities', 'url': '/static/docs/NSS Report/NSS Report/2023/18-Clean Campus Activities.pdf'},
        {'title': '19-Pledge-Life Style for Environment', 'url': '/static/docs/NSS Report/NSS Report/2023/19-Pledge-Life Style for Environment.pdf'},
        {'title': '20-Pledge on Drug Abuse and Illicit Trafficking', 'url': '/static/docs/NSS Report/NSS Report/2023/20-Pledge on Drug Abuse and Illicit Trafficking.pdf'},
    ]

    nss2022 = [
        {'title': 'NSS unit of National Institute of Technology Puducherry, Blood Donation camp', 'url': '/static/docs/NSS Report/NSS Report/2022/Blood donation Report 2022.pdf'},
    ]

    nss2021 = [
        {'title': 'Campus Cleaning and Seeds Sowing', 'url': '/static/docs/NSS Report/NSS Report/26 - Campus Cleaning and Seeds Sowing.pdf'},
        {'title': 'Awareness Campaigns on HIV & TB', 'url': '/static/docs/NSS Report/NSS Report/25 - Awareness Campaigns on HIV & TB.pdf'},
        {'title': 'Gandhi Jayanti 2021', 'url': '/static/docs/NSS Report/NSS Report/24 - Gandhi Jayanti 2021.pdf'},
    ]

    nss2020 = [
        {'title': 'Awareness Rally on AIDS Awareness Day', 'url': '/static/docs/NSS Report/NSS Report/23 - Awareness Rally on AIDS Awareness Day.pdf'},
        {'title': 'SWACCHATA PAKHWADA 2020', 'url': '/static/docs/NSS Report/NSS Report/22 - SWACCHATA PAKHWADA 2020.pdf'},
    ]
    nss2019 = [
        {
            'title': 'Vigilance Awareness Week-2019',
            'url': '/static/docs/NSS Report/NSS Report/21 - Vigilance Awareness Week-2019.pdf'
        },
        {
            'title': 'Swacchata Pakhwade - 2019',
            'url': '/static/docs/NSS Report/NSS Report/20 - Swacchata Pakhwade - 2019.pdf'
        },
        {
            'title': 'Swacchata Hi Seva - 2019',
            'url': '/static/docs/NSS Report/NSS Report/19 - Swacchata Hi Seva - 2019.pdf'
        },
        {
            'title': 'Rally on the Awareness on Eye Donation',
            'url': '/static/docs/NSS Report/NSS Report/18 - Rally on the Awareness on Eye Donation.pdf'
        },
        {
            'title': 'LEAP Sep; 2019 - Entrance Exam',
            'url': '/static/docs/NSS Report/NSS Report/17 - LEAP Sep; 2019 - Entrance Exam.pdf'
        },
        {
            'title': 'NIT-PY donates Blood@GH',
            'url': '/static/docs/NSS Report/NSS Report/16 - NIT-PY donates Blood@GH.pdf'
        },
        {
            'title': ' Campus Cleaning',
            'url': '/static/docs/NSS Report/NSS Report/15 - Campus Cleaning.pdf'
        },
        {
            'title': 'Visit to Karaikal Port',
            'url': '/static/docs/NSS Report/NSS Report/14 - Visit to Karaikal Port.pdf'
        },
        {
            'title': 'Friends of Police',
            'url': '/static/docs/NSS Report/NSS Report/13-Friends of Police.pdf'
        },
        {
            'title': 'Report-2019',
            'url': '/static/docs/NSS Report/NSS Report/12-SBSI2019REPORT.pdf'
        },
        {
            'title': 'Road Safety Week 2019',
            'url': '/static/docs/NSS Report/NSS Report/11 - Road Safety Week 2019.pdf'
        },
        {
            'title': 'NIT Puducherry donates Blood',
            'url': '/static/docs/NSS Report/NSS Report/10 -NIT Puducherry donates Blood.pdf'
        },
    ]
    req_roles = Role.objects.filter(role__icontains="NSS").select_related('id') 

    # Get unique staff members from those roles
    staff_ids = req_roles.values_list('id', flat=True).distinct()
    staff_list = Staff.objects.filter(id__in=staff_ids)

    # Optionally, get the relevant role for each staff (for display)
    staff_roles = {role.id_id: role for role in req_roles}

    context = {
        'nss2025': nss2025, 
        'nss2024': nss2024,
        'nss2023': nss2023,
        'nss2022': nss2022,
        'nss2021': nss2021,
        'nss2020': nss2020,
        'nss2019': nss2019,
        'staff_list': staff_list,
        'staff_roles': staff_roles,  # Map staff.id to their welfare role
    }
    

    return render(request, "students/nss.html", context)

def medical(request):
    Medical = [
        {"pic": "/static/images/medical/img001.jpg", "name": "ECG Machine (Electrocardiogram)"},
        {"pic": "/static/images/medical/img002.jpg", "name": "AED (Automated External Defibrillator)"},
        {"pic": "/static/images/medical/img003.jpg", "name": "Oxygen Cylinder with Trolley"},
        {"pic": "/static/images/medical/img004.jpg", "name": "Nebulizer Machine"},
        {"pic": "/static/images/medical/img005.jpg", "name": "Physical Examination Tray"},
        {"pic": "/static/images/medical/img006.jpg", "name": "Dressing and suturing Tray"},
        {"pic": "/static/images/medical/img007.jpg", "name": "Urinary Catheterization Tray"},
        {"pic": "/static/images/medical/img008.jpg", "name": "Intravenous Catheterization Tray"},
        {"pic": "/static/images/medical/img009.jpg", "name": "Emergency equipment"},
        {"pic": "/static/images/medical/img010.jpg", "name": "Glucometer"},
        {"pic": "/static/images/medical/img011.jpg", "name": "Portable Hemoglobin meter"},
        {"pic": "/static/images/medical/img012.jpg", "name": "Waiting area"},
        {"pic": "/static/images/medical/img013.jpg", "name": "Nurses Station"},
        {"pic": "/static/images/medical/img014.jpg", "name": "Observation Room"},
        {"pic": "/static/images/medical/img015.jpg", "name": "Consulting Room"},
        {"pic": "/static/images/medical/img016.jpg", "name": ""},
    ]
    req1 = Role.objects.filter(role__icontains="Chairman - Medical Care Committee").select_related('id') 
    req2 = Role.objects.filter(role__icontains="Member-Medical Care Committee").select_related('id')
    req_roles = req1 | req2  # Correct way to combine QuerySets

    # Get unique staff members from those roles
    staff_ids = req_roles.values_list('id', flat=True).distinct()
    staff_list = Staff.objects.filter(id__in=staff_ids)

    # Optionally, get the relevant role for each staff (for display)
    staff_roles = {role.id_id: role for role in req_roles}

    dept_staff_qs = Staff.objects.filter(department__icontains="Health Centre")
    staff_ids1 =  set(dept_staff_qs.values_list('id', flat=True))
    staff_list1 = Staff.objects.filter(id__in=staff_ids1).prefetch_related('role_set')
    roles1 = Role.objects.filter(id__in=staff_ids1)
    staff_roles1 = {role.id_id: role for role in roles1}
    context = {
        'staff_list': staff_list,
        'staff_roles': staff_roles,  # Map staff.id to their welfare role
        'Medical': Medical,
        'staff_list1': staff_list1,
        'staff_roles1': staff_roles1,  # Map staff.id to their welfare role
    }
    return render(request, "students/medical.html", context)

