import React from "react";
import axios from 'axios'
import qs from 'qs'
import { cloneDeep } from 'lodash'

class Interviewee extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: '',
      event: '',
      start_date: '',
      end_date: '',
      start_hour: '',
      start_half: '',
      start_ampm: '',
      end_hour: '',
      end_half: '',
      end_ampm: ''
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
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
    try {
      var state = cloneDeep(this.state)
      Reflect.deleteProperty(state, 'error')
      var { data: data } = await axios.post('/admin/update',
        qs.stringify(state),
        { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
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
        <form name="admin_form" onSubmit={this.handleSubmit}>
          {/* event */}
          <label htmlFor="event">Name of Your Event:</label>
          <input
            type="text"
            id="event"
            name="event"
            className="field"
            required
            value={this.state.event}
            onChange={this.handleChange} />

          {/* start_date */}
          <label htmlFor="start_date">Start Date:</label>
          <input
            type="date"
            id="start_date"
            name="start_date"
            className="field"
            min="2018-01-01"
            max="2025-12-31"
            required
            value={this.state.start_date}
            onChange={this.handleChange} />

          {/* end_date */}
          <label htmlFor="end_date">End Date:</label>
          <input
            type="date"
            id="end_date"
            name="end_date"
            className="field"
            min="2018-01-01"
            max="2025-12-31"
            required
            value={this.state.end_date}
            onChange={this.handleChange}
          />

          <label htmlFor="start_time">No Earlier Than:</label>
          <p>
            {/* start_hour */}
            <select
              type="number"
              id="start_hour"
              name="start_hour"
              required
              value={this.state.start_hour}
              onChange={this.handleChange}>
              <option></option>
              <option value={0}>0</option>
              <option value={2}>1</option>
              <option value={4}>2</option>
              <option value={6}>3</option>
              <option value={8}>4</option>
              <option value={10}>5</option>
              <option value={12}>6</option>
              <option value={14}>7</option>
              <option value={16}>8</option>
              <option value={18}>9</option>
              <option value={20}>10</option>
              <option value={22}>11</option>
            </select> :

            {/* start_half */}
            <select type="number"
              id="start_half"
              name="start_half"
              required
              value={this.state.start_half}
              onChange={this.handleChange}>
              <option></option>
              <option value={0}>00</option>
              <option value={1}>30</option>
            </select>

            {/* start_ampm */}
            <select
              type="number"
              id="start_ampm"
              name="start_ampm"
              required
              value={this.state.start_ampm}
              onChange={this.handleChange}
            >
              <option></option>
              <option value={0}>AM</option>
              <option value={1}>PM</option>
            </select>
          </p>

          <label htmlFor="end_time">No Later Than:</label>
          <p>
            {/* end_hour */}
            <select
              type="number"
              id="end_hour"
              name="end_hour"
              required
              value={this.state.end_hour}
              onChange={this.handleChange}
            >
              <option></option>
              <option value={0}>0</option>
              <option value={2}>1</option>
              <option value={4}>2</option>
              <option value={6}>3</option>
              <option value={8}>4</option>
              <option value={10}>5</option>
              <option value={12}>6</option>
              <option value={14}>7</option>
              <option value={16}>8</option>
              <option value={18}>9</option>
              <option value={20}>10</option>
              <option value={22}>11</option>
            </select> :

            {/* end_half */}
            <select
              type="number"
              id="end_half"
              name="end_half"
              required
              value={this.state.end_half}
              onChange={this.handleChange}
            >
              <option></option>
              <option value={0}>00</option>
              <option value={1}>30</option>
            </select>

            {/* end_ampm */}
            <select
              type="number"
              id="end_ampm"
              name="end_ampm"
              required
              value={this.state.end_ampm}
              onChange={this.handleChange}
            >
              <option></option>
              <option value={0}>AM</option>
              <option value={1}>PM</option>
            </select>
          </p>

          <p className={this.state.error ? "error" : 'error error--hidden'}>{this.state.error}</p>
          <input type="submit" value="Submit" className="btn" />
        </form>
      </div>
    )
  };
}

export default Interviewee