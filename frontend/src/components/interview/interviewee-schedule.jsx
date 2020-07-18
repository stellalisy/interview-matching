import React from "react";
import dayjs from 'dayjs'

class IntervieweeSchedule extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    var result = this.props
    var start_date = result['start_date'];
    var start_time = result['start_time'];
    var days = result['days'];
    var hours = result['hours'];
    var time = result['final_time'];

    var day = Math.floor(time / hours);
    var time_slot = (time - day * hours) % hours + parseInt(start_time, 10);
    var half = time_slot % 2 ? ":30" : ":00";
    if (time_slot < 24) {
      var am = "AM";
      var hour = Math.floor(time_slot / 2);
    } else {
      var am = "PM";
      var hour = Math.floor((time_slot - 24) / 2);
    }
    var date = dayjs(start_date).add(day, 'day');
    var final = date.format('MM/DD') + " " + hour.toString(10) + half + am;

    return (
      <div className="card">
        <h1 className="center">Scheduled Interview</h1>
        <p><strong>Name:</strong> {this.props.name}</p>
        <p><strong>Interest 1:</strong>  {this.props.interest1}</p>
        <p><strong>Interest 2:</strong> {this.props.interest2}</p>
        <p id="interview_time"><strong>Interview Time: {final}</strong></p>
        <div className="center">
          <br /><a href="#!" onClick={() => this.props.callback()} className="btn btn--secondary">Sign Out</a>
        </div>
      </div>
    )
  }
}

export default IntervieweeSchedule