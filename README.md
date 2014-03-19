Cloud Assignment

Andrew Cox, c11401898
lit-anchorage-6910.herokuapp.com




This is a RESTful Calendar system  implemented in Flask.

This is an assignment for a college module called Cloud Computing in DIT.

This is only for educational purposes.




Documentation:

The API take each request and return a json status message. There are error fields in place in case something goes wrong.

There are four methods in the API:
GET, POST, DELETE and PUT.

Each of these will have an example input and output further down.

Parameters used by me:
  Calid: CalenderID for calender identity
  Taskid: for task identity
  Values: Entries Dictionaries' name



Test Exaples:
  These tests are all in the repository.
  They are the use of simple curl commands on a local host.
  
CalendarCreate:
  Input:
  
    curl -X POST  http://localhost:5000/calender/1

    curl -X POST  http://localhost:5000/calender/2
  
    curl -i GET  http://localhost:5000/calender
  
  Output:
  
    {
      "calender_list": [
      {
        "CalID": 2, 
        "Values": []
      }, 
      {
        "CalID": 1, 
        "Values": []
      }
    ]


This shows the simple commands required to create calenders.
  
CreateEntries:
  Input:
  
    curl -X POST http://localhost:5000/calender/1

    curl -X POST -d '{}'  http://localhost:5000/calender/1/task/1

    curl -X POST -d ''  http://localhost:5000/calender/1/task/2

    curl -i GET  http://localhost:5000/calender/1

  Output:
  
    {
      "calender_list": [
      {
        "CalID": 1, 
        "Values": [
          {
            "TaskID": 1, 
            "description": "", 
            "end_time": "", 
            "location": "", 
            "repeats": 0, 
            "start_time": "", 
            "title": ""
          }, 
          {
            "TaskID": 2, 
            "description": "", 
            "end_time": "", 
            "location": "", 
            "repeats": 0, 
            "start_time": "", 
            "title": ""
          }
        ]
      } 
    ]


This shows the creation of two tasks into one Calendar.
  
CreateEntryVal:
  Input:
  
    curl -X POST http://localhost:5000/calender/1

    curl -X POST -d '{}'  http://localhost:5000/calender/1/task/1

    curl -X POST -d '{"title":"Home and Away"}'  http://localhost:5000/calender/1/task/2

    curl -i GET  http://localhost:5000/calender/1
    
  Output:
  
    {
    "CalID": 1, 
    "Values": [
      {
        "TaskID": 1, 
        "description": "", 
        "end_time": "", 
        "location": "", 
        "repeats": 0, 
        "start_time": "", 
        "title": ""
      }, 
      {
        "TaskID": 2, 
        "description": "", 
        "end_time": "", 
        "location": "", 
        "repeats": 0, 
        "start_time": "", 
        "title": "Home and Away"
      }
    ]
  

This shows entry of Home and Away into the 2 task only.
  
SelectEntry:
  Input:
  
    curl -X POST http://localhost:5000/calender/1

    curl -X POST -d '{}'  http://localhost:5000/calender/1/task/1
    
    curl -X POST -d '{}'  http://localhost:5000/calender/1/task/2
    
    curl -i GET  http://localhost:5000/calender/1/task/2

  Output:
  
    {
    "TaskID": 2, 
    "description": "", 
    "end_time": "", 
    "location": "", 
    "repeats": 0, 
    "start_time": "", 
    "title": ""
  
  This shows the selection of one set of entries even though there are more.
  
DeleteCalendar:
  Input:
  
    curl -X POST  http://localhost:5000/calender/1

    curl -X POST  http://localhost:5000/calender/2
    
    curl -i GET  http://localhost:5000/calender
    
    curl -X DELETE  http://localhost:5000/calender/1
    
    curl -i GET  http://localhost:5000/calender

  Output:
  
    {
    "calender_list": [
      {
        "CalID": 2, 
        "Values": []
      }
    ]
  
  This shows the creation of two calendars and the deletion of one of them.
  
DeleteEntry:
  Input:
  
    curl -X POST  http://localhost:5000/calender/1

    curl -X POST -d '{}'  http://localhost:5000/calender/1/task/1
    
    curl -X POST -d '{}'  http://localhost:5000/calender/1/task/2
    
    curl -i GET  http://localhost:5000/calender
    
    curl -X DELETE  http://localhost:5000/calender/1/task/1
    
    curl -i GET  http://localhost:5000/calender

    
  Output:
  
    {
    "calender_list": [
      {
        "CalID": 2, 
        "Values": []
      }, 
      {
        "CalID": 1, 
        "Values": [
          {
            "TaskID": 2, 
            "description": "", 
            "end_time": "", 
            "location": "", 
            "repeats": 0, 
            "start_time": "", 
            "title": ""
          }
        ]
      }
    ]
  
  This shows the creation of two entries in a calender and the deletion of one.
