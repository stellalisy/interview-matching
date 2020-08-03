import React from "react";
import axios from './request'
import qs from 'qs'

class Login extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: '',
      email: '',
      password: '',
    };

    this.handleChange = this.handleChange.bind(this);
    this.login = this.login.bind(this);
  }

  handleChange(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;
    this.setState({
      [name]: value
    });
  }

  // log in
  async login(e, checkSchedule = false) {
    e.preventDefault();
    var { email, password } = this.state
    try {
      var { data: data } = await axios.post('/user/login',
        qs.stringify({ email, password }),
        { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } }
      )
      var error = data.error
      if (error && error !== 'false') {
        this.setState({ error })
      } else {
        this.props.callback(data, checkSchedule)
      }
    } catch (err) {
      console.log(err)
    }
  }

  render() {
    return (
      <div className="card">
        <h1 className="center">Log In</h1>
        <form name="login_form">

          {/* email */}
          <label htmlFor="email">Email</label>
          <input type="email"
            name="email"
            value={this.state.email}
            className="field"
            onChange={this.handleChange} required />

          {/* password */}
          <label htmlFor="password">Password</label>
          <input
            type="password"
            name="password"
            value={this.state.password}
            className="field"
            onChange={this.handleChange}
            required />

          <p className={this.state.error ? "error" : 'error error--hidden'}>{this.state.error}</p>

          <button onClick={this.login} className="btn-left" >Log In</button>
          <button onClick={e => this.login(e, true)} className="btn-right">Interview Schedule</button>
        </form>
      </div>)
  };
}

export default Login