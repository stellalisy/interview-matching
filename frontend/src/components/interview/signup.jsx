import React from "react";
import axios from 'axios'
import qs from 'qs'

class Signup extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: '',
      name: '',
      email: '',
      password: '',
      password2: '',
      role: 'Interviewer',
    };

    this.handleChange = this.handleChange.bind(this);
    this.signup = this.signup.bind(this);
  }


  handleChange(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;
    this.setState({
      [name]: value
    });
  }

  // sign up
  async signup(e) {
    e.preventDefault();
    var {
      name,
      email,
      password,
      password2,
      role
    } = this.state
    try {
      var { data: data } = await axios.post('/user/signup',
        qs.stringify({ name, email, password, password2, role }),
        { headers: { 'Content-Type': 'application/x-www-form-urlencoded' } },
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
        <h1 className="center">Create an Account</h1>
        <form name="signup_form" onSubmit={this.signup}>

          {/* name */}
          <label htmlFor="name">Name</label>
          <input
            type="text"
            name="name"
            value={this.state.name}
            className="field"
            onChange={this.handleChange}
            required />

          {/* email */}
          <label htmlFor="email">Email</label>
          <input
            type="email"
            name="email"
            value={this.state.email}
            className="field"
            onChange={this.handleChange}
            required />

          {/* password */}
          <label htmlFor="password">Password</label>
          <input type="password"
            name="password"
            value={this.state.password}
            className="field"
            onChange={this.handleChange} required />

          {/* Repeat Password */}
          <label htmlFor="password2">Repeat Password</label>
          <input
            type="password"
            name="password2"
            value={this.state.password2}
            className="field"
            onChange={this.handleChange} required />

          {/* role */}
          <label htmlFor="role">Interviewer/Interviewee</label>
          <p>
            <select name='role' value={this.state.role} onChange={this.handleChange}>
              <option></option>
              <option value="Interviewer">Interviewer</option>
              <option value="Interviewee">Interviewee</option>
              <option value="Admin">Admin</option>
            </select>
          </p>

          <p className={this.state.error ? "error" : 'error error--hidden'}>{this.state.error}</p>
          <input type="submit" value="Sign Up" className="btn" />
        </form>
      </div>)
  };
}

export default Signup