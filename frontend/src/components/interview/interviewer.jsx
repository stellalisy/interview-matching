import React from "react";
import axios from './request'
import qs from 'qs'
import dayjs from 'dayjs'

class Interviewer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: '',
      start_date: '',
      start_time: null,
      days: 0,
      hours: 0,
      grid: [],
      max_int: '',
      team: '',
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
    var { max_int, grid, team } = this.state
    try {
      var { data: data } = await axios.post('/interviewer/update',
        { max_int, grid, team }
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
        <form name="interviewer_form" id="interviewer_form" onSubmit={this.handleSubmit}>
          <label htmlFor="max_int">Maximum number of interviews you can do:</label>
          <p>
            <select name='max_int' className="field" value={this.state.max_int} onChange={this.handleChange}>
              <option></option>
              <option value={4}>4</option>
              <option value={5}>5</option>
              <option value={6}>6</option>
              <option value={7}>7</option >
              <option value={8}>8</option >
            </select >
          </p >

          <label htmlFor="team">Which team are you on:</label>
          <p>
            <select name='team' className="field" value={this.state.team} onChange={this.handleChange}>
              <option></option>
              <option value="Logistics">Transport/Logistics/Food</option>
              <option value="Social/PR">Social/PR</option>
              <option value="Sponsors">Sponsors</option>
              <option value="Website">Website</option>
              <option value="Design">Design</option>
              <option value="Membership">Membership</option>
            </select>
          </p>

          <label htmlFor="time">Time Available (please select all that apply):</label>

          <div className="row">
            <span className="row-cell" key={`row-null`}></span>
            {Array.from({length:this.state.days}).map((o2, i2) => {
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
                    Math.floor((this.state.start_time % 24) / 2) + Math.floor(i1 / 2) + ":30" + (this.state.start_time < 24 ? "AM" : "PM") : 
                    Math.floor((this.state.start_time % 24) / 2) + Math.floor(i1 / 2) + ":00" + (this.state.start_time < 24 ? "AM" : "PM")}
                </span>
                {Array.from({ length: this.state.days }).map((o2, i2) => {
                  return (
                    <span className={this.state.grid[i1][i2] ? 'cell selected' : 'cell'}
                      key={`${i1}-${i2}`}
                      onClick={() => this.toggle(i1, i2)}>
                    </span>
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

export default Interviewer