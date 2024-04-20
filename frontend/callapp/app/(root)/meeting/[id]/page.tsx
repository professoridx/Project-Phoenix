import React from 'react'
const Mettings = ({ params }: { params: { id: string } })=> {
    return(
        <div> Meeting Room : #{params.id}</div>
    )
}
export default Mettings