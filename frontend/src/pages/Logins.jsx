import { useEffect, useState } from "react";

import {
    getLogins
} from "../services/api";


function Logins() {

    const [logins, setLogins] =
        useState([]);


    useEffect(() => {

        getLogins()
            .then(response => {

                setLogins(
                    response.data
                );

            });

    }, []);


    return (

        <main>

            <h1>Login Security</h1>

            <table>

                <thead>

                    <tr>

                        <th>Customer</th>
                        <th>IP Address</th>
                        <th>Location</th>
                        <th>Device</th>
                        <th>Status</th>
                        <th>Risk</th>

                    </tr>

                </thead>


                <tbody>

                    {logins.map(
                        login => (

                        <tr
                            key={login.id}
                        >

                            <td>
                                {
                                    login.customer_id
                                }
                            </td>

                            <td>
                                {
                                    login.ip_address
                                }
                            </td>

                            <td>
                                {
                                    login.location
                                }
                            </td>

                            <td>
                                {
                                    login.device_id
                                }
                            </td>

                            <td>

                                {
                                    login.success
                                        ? "Success"
                                        : "Failed"
                                }

                            </td>

                            <td>

                                {
                                    login.risk_level
                                }

                                {" "}

                                (
                                {
                                    login.risk_score
                                }
                                )

                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </main>
    );
}

export default Logins;