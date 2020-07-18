import React from "react";
import axios from 'axios'
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
  async login(e) {
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
        this.props.callback(data)
      }
    } catch (err) {
      console.log(err)
    }
  }

  render() {
    return (
      <div className="card">
        <h1 className="center">Log In</h1>
        <form name="login_form" onSubmit={this.login}>

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

          <input type="submit" value="Log In" className="btn" />
        </form>
      </div>)
  };
}

export default Login