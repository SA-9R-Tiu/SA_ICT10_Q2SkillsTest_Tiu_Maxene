from pyscript import display, document

# Define club information using dictionaries
club_info = {
            "dance": {
                "name": "Dance Club",
                "description": "A club for dance enthusiasts of all dance levels and genres.",
                "meeting_time": "Every MWF 3:30-5:30 PM",
                "location": "Room 17",
                "advisor": "Mr. Kwon",
                "members": 20,
                "category": "Arts"
            },
            "drama": {
                "name": "Drama Club",
                "description": "For students interested in theater, acting, and stage production.",
                "meeting_time": "Every Monday and Thursday 2:00-4:00 PM",
                "location": "SVT Hall",
                "advisor": "Mr. Wen",
                "members": 13,
                "category": "Arts"
            },
            "english": {
                "name": "English Club",
                "description": "For students that wants to improve their speech, reading, and writing skills.",
                "meeting_time": "Every Tuesday 12:45-2:45 PM",
                "location": "Club room 107",
                "advisor": "Mr. Hong",
                "members": 17,
                "category": "Academic"
            },
            "debate": {
                "name": "Debate Club",
                "description": "Develop public speaking and argumentation skills.",
                "meeting_time": "Every Friday 1:30-3:00 PM",
                "location": "Room 507",
                "advisor": "Mr. Choi",
                "members": 12,
                "category": "Academic"
            },
            "art": {
                "name": "Art Club",
                "description": "Explore various art mediums and techniques.",
                "meeting_time": "Every Wednesday 3:45-5:15 PM",
                "location": "Art Room",
                "advisor": "Mr. Xu",
                "members": 20,
                "category": "Arts"
            },
            "glee": {
                "name": "Glee Club",
                "description": "To enhance and showcase the singing skills of the students.",
                "meeting_time": "Every Tuesday and Thursday 12:30-3:00 PM",
                "location": "Music Room",
                "advisor": "Mr. Kim",
                "members": "27",
                "category": "Arts"
            }                                                                                                                                                           
        }   
        
def show_club_info(e):
    document.getElementById('club-info').innerHTML = " "
    selected_club = document.getElementById("club-select").value
    info = club_info.get(selected_club, club_info["dance"])
            
    output = f"""
            {info['name']}
            Description:{info['description']}
            Meeting Time: {info['meeting_time']}
            Location: {info['location']}
            Advisor: {info['advisor']}
            Number of Members: {info['members']}
            Category: {info['category']}
            """
    display(output, target="club-info")