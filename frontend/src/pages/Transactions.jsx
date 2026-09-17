import { useEffect, useState } from "react";

import {
    getTransactions
} from "../services/api";


function Transactions() {

    const [transactions, setTransactions]
        = useState([]);


    useEffect(() => {

        getTransactions()
            .then(response => {

                setTransactions(
                    response.data
                );

            });

    }, []);


    return (

        <main>

            <h1>Transaction Monitoring</h1>

            <table>

                <thead>

                    <tr>

                        <th>ID</th>
                        <th>Customer</th>
                        <th>Amount</th>
                        <th>Location</th>
                        <th>Merchant</th>
                        <th>Risk</th>
                        <th>Reason</th>

                    </tr>

                </thead>


                <tbody>

                    {transactions.map(
                        transaction => (

                        <tr
                            key={
                                transaction.id
                            }
                        >

                            <td>
                                {
                                    transaction
                                    .transaction_id
                                }
                            </td>

                            <td>
                                {
                                    transaction
                                    .customer_id
                                }
                            </td>

                            <td>
                                ₹
                                {
                                    transaction.amount
                                }
                            </td>

                            <td>
                                {
                                    transaction.location
                                }
                            </td>

                            <td>
                                {
                                    transaction.merchant
                                }
                            </td>

                            <td>

                                <span
                                    className={
                                        transaction
                                        .risk_level
                                        .toLowerCase()
                                    }
                                >

                                    {
                                        transaction
                                        .risk_level
                                    }

                                    {" "}
                                    (
                                    {
                                        transaction
                                        .risk_score
                                    }
                                    )

                                </span>

                            </td>

                            <td>
                                {
                                    transaction.reason
                                }
                            </td>

                        </tr>

                    ))}

                </tbody>

            </table>

        </main>
    );
}

export default Transactions;