import React from "react";
import axios from 'axios'
import { Login, Signup, TopHeader, Interviewee, Interviewer, Admin, UserInfo, Success } from './interview/index'
import '../css/styles.css'
import '../css/normalize.css'

class Interview extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      user: null, // user's role: Interviewee | Interviewer | Admin
      success: false,
    };

    this.setUser = this.setUser.bind(this);
    this.signout = this.signout.bind(this);
    this.onSuccess = this.onSuccess.bind(this);
    this.onBack = this.onBack.bind(this);
  }

  setUser(user) {
    this.setState({ user })
  }

  async signout() {
    try {
      await axios.get('/user/signout')
      this.setState({ user: null, success: false })
    } catch (err) {
      console.log(err)
    }
  }

  onSuccess() {
    this.setState({ success: true })
  }

  onBack() {
    this.setState({ success: false })
  }

  // componentDidMount() {
  //     // this.request = $.get(this.props.url, (result) {
  //     //     var { start_date, end_date, start_time, end_time } = result;
  //     //     this.setState({
  //     //         start_date, end_date, start_time, end_time
  //     //     });
  //     // }.bind(this));
  //     var start_date = '2020-07-01'
  //     var end_date = '2020-07-05'
  //     var start_time = 9
  //     var end_time = 15
  //     var days = dayjs(end_date).diff(dayjs(start_date), 'day')
  //     var hours = end_time - start_time
  //     var grid = Array(hours * 2).fill(0).map(item => Array(days).fill(0))

  //     this.setState({
  //         start_date,
  //         start_time,
  //         grid,
  //         days,
  //         hours,
  //     });
  // }

  // toggle(i1, i2) {
  //     var { grid } = this.state
  //     grid[i1][i2] = grid[i1][i2] ? 0 : 1
  //     this.setState({ grid })
  // }

  // handleChange(event) {
  //     const target = event.target;
  //     const value = target.value;
  //     const name = target.name;

  //     this.setState({
  //         [name]: value
  //     });
  // }

  render() {
    var { user, success } = this.state
    var role = user && user.role
    var User

    if (role === 'Interviewee') {
      User = <Interviewee callback={this.onSuccess} />
    } else if (role === 'Interviewer') {
      User = <Interviewer callback={this.onSuccess} />
    } else if (role === 'Admin') {
    User = <Admin callback={this.onSuccess} />
    }

    return (
      <div>
        <TopHeader role={role} />

        <div className="card-wrapper">
          {
            user ?
              (success ?
                <Success callback={this.signout} back={this.onBack} /> :
                <>
                  <UserInfo  {...user} callback={this.signout} />
                  {User}
                </>
              ) :
              <>
                <Signup callback={this.setUser} />
                <Login callback={this.setUser} />
              </>
          }
        </div>
      </div>
    )
  };
}

export default Interview