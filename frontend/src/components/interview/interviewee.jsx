import React from "react";
import qs from 'qs'
import dayjs from 'dayjs'
import axios from './request'
import cloneDeep from 'lodash';

class Interviewee extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: '',
      start_date: '',
      start_time: null,
      days: 0,
      hours: 0,
      grid: null,
      interest1: '',
      interest2: ''
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  componentDidMount() {
    var {
      start_date,
      start_time,
      days,
      hours
    } = this.props

    this.setState({
      start_date,
      start_time,
      days,
      hours,
      grid: Array(hours * 2).fill(0).map(() => Array(days).fill(0))
    })
  }

  toggle(i1, i2) {
    var { grid } = this.state
    grid[i1][i2] = grid[i1][i2] ? 0 : 1
    this.setState({ grid })
  }

  handleChange(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;
    this.setState({
      [name]: value
    });
  }

  async handleSubmit(e) {
    e.preventDefault();
    var { interest1, grid, interest2 } = this.state
    try {
      var { data: data } = await axios.post('/api/interviewee/update',
        { interest1, grid, interest2 }
      )
      var error = data.error
      if (error && error !== 'false') {
        this.setState({ error })
      } else {
        this.props.callback(data)
      }
    } catch (err) {
      console.log(err)
    }
  }

  render() {
    return (
      <div className="card">
        <h1 className="center">Availability</h1>
        <form name="interviewee_form" id="interviewee_form" onSubmit={this.handleSubmit}>
          <label htmlFor="year">Graduation Year</label>
          <input type="year" name="year" className="field" required />

          <label htmlFor="interest1">Interest 1</label>
          <p>
            <select name='interest1' className="field" value={this.state.interest1} onChange={this.handleChange}>
              <option></option>
              <option value="Logistics">Transport/Logistics/Food</option>
              <option value="Social/PR">Social/PR</option>
              <option value="Sponsors">Sponsors</option>
              <option value="Website">Website</option>
              <option value="Design">Design</option>
              <option value="Membership">Membership</option>
            </select>
          </p>

          <label htmlFor="interest2">Interest 2</label>
          <p>
            <select name='interest2' className="field" value={this.state.interest2} onChange={this.handleChange}>
              <option></option>
              <option value="Logistics">Transport/Logistics/Food</option>
              <option value="Social/PR">Social/PR</option>
              <option value="Sponsors">Sponsors</option>
              <option value="Website">Website</option>
              <option value="Design">Design</option>
              <option value="Membership">Membership</option>
            </select>
          </p>

          <label htmlFor="time">Time Available (please select all that apply): </label>

          <div className="row">
            <span className="row-cell" key={`row-null`}></span>
            {Array.from({ length: this.state.days }).map((o2, i2) => {
              return (
                <span key={`header-${i2}`} className="header-date">
                  {dayjs(this.state.start_date).add(i2, 'day').format('MM/DD')}
                </span>
              )
            })}
          </div>
          {Array.from({ length: this.state.hours }).map((o1, i1) => {
            return (
              <div key={`${i1}`} className="row">
                <span className="row-cell" key={`row-${i1}`}>
                  {(this.state.start_time + i1) % 2 ?
                    Math.floor((this.state.start_time % 24) / 2) +
                    i1 / 2 + ":30" +
                    (this.state.start_time < 24 ? "AM" : "PM") :
                    (this.state.start_time % 24) / 2 + i1 / 2 + ":00" +
                    (this.state.start_time < 24 ? "AM" : "PM")}
                </span>
                {Array.from({ length: this.state.days }).map((o2, i2) => {
                  return (
                    <span className={this.state.grid[i1][i2] ? 'cell selected' : 'cell'}
                      key={`${i1}-${i2}`}
                      onClick={() => this.toggle(i1, i2)}
                    ></span>
                  )
                })}
              </div>
            )
          })}
          <p className={this.state.error ? "error" : 'error error--hidden'}>{this.state.error}</p>
          <input type="submit" value="Submit" className="btn" />
        </form>
      </div>
    )
  };
}

export default Interviewee