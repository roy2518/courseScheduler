import React, { Fragment } from 'react'
import {Segment, Button} from 'semantic-ui-react'
import {client} from '../constants/api'


class ScheduleList extends React.Component {

    state = {
        schedules: []
    }

    getSchedules = async (netid) => {
        let response = await client.get(`/schedule/${netid}`)
        if (response.status % 200 > 100) {
            throw ('error')
        }
        this.setState({ schedules: response.data })
    }

    renderSchedules = (schedules) => {

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
                        <Button floated='right'
                            schedule={schedule}
                            onClick={(e, { schedule }) => { this.props.loadSchedule(schedule) }}
                        >
                            Load
                        </Button>
                        <Button floated='right' disabled>
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