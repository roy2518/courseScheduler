import React, { Fragment } from 'react'
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'

import '../css/main.scss'

class Calendar extends React.Component {


    generateEvents = (courses) => {
        return courses.map((course) => {
            let courseEvent = {
                title: `${course.subject} ${course.course_num} / ${course.type}`,
                daysOfWeek: [],
                startTime: course.start_time,
                endTime: course.end_time,
                start: new Date()
            }
    
            if (course.days.mon === true) {
                courseEvent.daysOfWeek.push(1)
            }
            if (course.days.tues === true) {
                courseEvent.daysOfWeek.push(2)
            }
            if (course.days.wed === true) {
                courseEvent.daysOfWeek.push(3)
            }
            if (course.days.thur === true) {
                courseEvent.daysOfWeek.push(4)
            }
            if (course.days.fri === true) {
                courseEvent.daysOfWeek.push(5)
            }
    
            return courseEvent
        })
    }

    render() {
        
        return (
            <Fragment>
                <FullCalendar
                    defaultView="timeGridWeek" 
                    weekends={false}
                    plugins={[ timeGridPlugin ]}
                    allDaySlot={false}
                    minTime="08:00:00"
                    maxTime="22:00:00"
                    events={this.generateEvents(this.props.courses)}
                />
            </Fragment>
           
        )
    }
}


export default Calendar