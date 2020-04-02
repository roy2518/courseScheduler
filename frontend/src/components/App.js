import React, {Fragment} from 'react'
import {Grid, Segment} from 'semantic-ui-react'
import ClassSearch from './ClassSearch'
import Calendar from './Calendar'


class App extends React.Component {

    constructor(props) {
        super(props)
        this.addCourse = this.addCourse.bind(this)
    }

    state = {
        courses: {}
    }

    addCourse = (course) => {
        let courseEvent = {}

        courseEvent.title
        courseEvent.daysOfWeek
    }

    render() {
        return (
            <Fragment>
                <div style={{position: "relative", boxShadow: "0 3px 4px -6px gray"}}>
                    <Grid columns={2}>
                        <Grid.Column width={8}>
                            <Segment basic padded>
                                <Calendar courses={this.state.courses}/>
                            </Segment>
                        </Grid.Column>
                        <Grid.Column width={5} style={{minWidth: "340px"}}>
                            <ClassSearch addCourse={this.addCourse}/>
                        </Grid.Column>
                    </Grid>
                </div>
            </Fragment>
        )
    }
}

export default App