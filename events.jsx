import React from 'react';

class Events extends React.Component {
  constructor(props) {
    super(props);
    this.state = {events: [],
                  isLoading: false,
                  error: null};
  }

  componentDidMount() {
    this.setState({ isLoading: true });
    fetch(this.props.url)
      .then(response => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error('Something went wrong ...');
        }
      })
      .then(data => this.setState({ events: data, isLoading: false }))
      .catch(error => this.setState({ error, isLoading: false }));
  }

  render() {
  const { events, isLoading, error } = this.state;
  if (error) {
      return <p>{error.message}</p>;
  }
  if (isLoading) {
    return <div>Loading...</div>
  }

  return  <table className="table table-striped">
          <thead>
          <tr>
            <th>Time</th>
            <th>Kind</th>
            <th>Comment</th>
            <th></th>
          </tr>
          </thead>
          <tbody>
          {events.map((event) => <Event key={event.id} info={event} url={this.props.url} />)}
          </tbody>
        </table>
}
}

class Event extends React.Component {
  render() {
    const info = this.props.info
    return <tr>
            <td>{info.time}</td>
            <td>{info.name}</td>
            <td>{info.comment}</td>
            <td><a className="small" href={this.props.url + "delete/" + info.id}>delete</a></td>
          </tr>
  }
}

module.exports = {Events: Events}
