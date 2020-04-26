import React, { Fragment } from 'react'
import { Segment, Button, Loader } from 'semantic-ui-react'
import { client } from '../constants/api'


class ScheduleList extends React.Component {

    state = {
        schedules: [],
        loading: false
    }

    getSchedules = async (netid) => {
        this.setState({loading: true})
        let response = await client.get(`/schedule/${netid}`)
        if (response.status % 200 > 100) {
            this.setState({loading: false})
            throw ('error')
        }
        this.setState({ schedules: response.data, loading: false})
    }

    renderSchedules = (schedules) => {

        if (this.state.loading) {
            return <Segment style={{minHeight: '50px'}}><Loader active/></Segment>
        }

        if (schedules.length === 0) {
            return (
                <Segment>No schedules found</Segment>
            )
        }

        return (
            schedules.map((schedule) => {
                return (
                    <Segment>
                        Schedule #{schedule.sched_num}
                        <Button floated='right' color='blue'
                            schedule={schedule}
                            onClick={(e, { schedule }) => { this.props.loadSchedule(schedule) }}
                        >
                            Load
                        </Button>
                        <Button floated='right' color='red'
                            schedule={schedule}
                            onClick={async(e, { schedule }) => { 
                                if (await this.props.deleteSchedule(schedule) === true) {
                                    console.log('jerry')
                                    this.setState({schedules: this.state.schedules.filter((s) => schedule !== s)})
                                }}}
                        >
                            Delete
                        </Button>
                    </Segment>
                )
            })
        )
    }

    componentDidMount() {
        this.getSchedules(this.props.netid)
    }

    render() {
        return (
            <Fragment>
                {this.renderSchedules(this.state.schedules)}
            </Fragment>
        )
    }
}
export default ScheduleList