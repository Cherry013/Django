import React from 'react';
import { FaPhoneAlt, FaClock } from 'react-icons/fa';

const HeaderTop = () => {

    let d = new Date();
    let months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
    let month = months[d.getMonth()]
    let date = d.getDate();



    return (
        <div className="header-top pt-15 pb-15 bg-1">
            <div className="container">
                <div className="row">
                    <div className="col-xl-8 col-lg-8 col-md-12 col-sm-12">
                        <div className="header-info">
                            <ul>
                                <li>
                                    <i class="fa-solid fa-envelope"></i> 
                                    <span> econation.r20@gmail.com</span>
                                </li>
                            </ul>
                        </div>
                    </div>
                    <div className="col-xl-4 col-lg-4 col-md-12 col-sm-12">
                        <div className="header-social text-center text-xl-end text-lg-end">
                            <span> {month}, {date} </span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default HeaderTop;