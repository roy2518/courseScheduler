import React from 'react'
import FullCalendar from '@fullcalendar/react'
import dayGridPlugin from '@fullcalendar/daygrid'
import timeGridPlugin from '@fullcalendar/timegrid'

import '../css/main.scss'

class Calendar extends React.Component {

    render() {
        return (
            <FullCalendar
                defaultView="timeGridWeek" 
                weekends={false}
                plugins={[ timeGridPlugin ]}
                events={[
                    {title: 'dynamic event',
                    daysOfWeek: [1,4,5],
                    startTime: '09:00:00',
                    endTime: '14:00:00',
                    start: Date.now(),
                    },
                    {title: 'dynamic event',
                    daysOfWeek: [1,4,5],
                    startTime: '12:00:00',
                    endTime: '16:00:00',
                    start: Date.now(),
                    },
                    {title: 'dynamic event',
                    daysOfWeek: [1,4,5],
                    startTime: '11:00:00',
                    endTime: '16:00:00',
                    start: Date.now(),
                    }
                ]}
            />
        )
    }
}


export default Calendar