import React, { Fragment } from 'react'
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'

import '../css/main.scss'

class Calendar extends React.Component {


    render() {
        
        return (
            <Fragment>
                <FullCalendar
                    defaultView="timeGridWeek" 
                    weekends={false}
                    plugins={[ timeGridPlugin ]}
                    events={this.props.courses}
                />
                <list>{this.props.courses.map((c)=>{return(<li>{c.title}</li>)})}</list>
            </Fragment>
           
        )
    }
}


export default Calendar