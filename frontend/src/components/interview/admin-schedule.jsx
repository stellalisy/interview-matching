import React from "react";
import dayjs from 'dayjs'

class AdminSchedule extends React.Component {
  constructor(props) {
    super(props);
  }

  render() {
    var result = this.props
    var start_date = result['start_date'];
    var start_time = result['start_time'];
    var days = result['days'];
    var hours = result['hours'];
    var event = result['event'];
    var interviews = result['interviews'] || [];
    var num_int = interviews.length;
    var list = Array.from({ length: num_int })

    return (
      <div className="card">
        <h1 className="center">Interview Summary</h1>
        <table>
          <thead>
            <tr>
              <th></th>
              <th>Interviewee</th>
              <th>Time</th>
              <th>Interest 1</th>
              <th>Interest 2</th>
            </tr>
          </thead>
          <tbody id="tbody">
            {
              list.map((o, i) => {
                var time = interviews[i]['final_time'];
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

                var interviewer1 = interviews[i]['interviewers'][0]['team'] + ": " + interviews[i]['interviewers'][0]['name'];
                var interviewer2 = interviews[i]['interviewers'][1]['team'] + ": " + interviews[i]['interviewers'][1]['name'];

                return <tr>
                  <td>{i + 1}</td>
                  <td>{interviews[i]['name']}</td>
                  <td>{final}</td>
                  <td>{interviewer1}</td>
                  <td>{interviewer2}</td>
                </tr>;
              })
            }
          </tbody>
        </table>
        <div className="center">
          <br /><a href="#!" onClick={() => this.props.callback()} className="btn btn--secondary">Sign Out</a>
        </div>
      </div>
    )
  }
}

export default AdminSchedule