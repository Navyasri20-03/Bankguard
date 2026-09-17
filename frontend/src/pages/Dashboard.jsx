import { useEffect, useState } from "react";

import {
    getDashboardStats
} from "../services/api";

import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    CartesianGrid
} from "recharts";


function Dashboard() {

    const [stats, setStats] = useState({});

    useEffect(() => {

        getDashboardStats()
            .then(response => {
                setStats(response.data);
            });

    }, []);


    const data = [

        {
            name: "Transactions",
            value:
                stats.total_transactions || 0
        },

        {
            name: "Suspicious",
            value:
                stats.suspicious_transactions || 0
        },

        {
            name: "Failed Logins",
            value:
                stats.failed_logins || 0
        },

        {
            name: "High Risk",
            value:
                stats.high_risk_logins || 0
        }

    ];


    return (

        <main>

            <h1>Security Dashboard</h1>

            <div className="cards">

                <div className="card">

                    <h3>
                        Total Transactions
                    </h3>

                    <h2>
                        {stats.total_transactions || 0}
                    </h2>

                </div>


                <div className="card">

                    <h3>
                        Suspicious Transactions
                    </h3>

                    <h2>
                        {stats.suspicious_transactions || 0}
                    </h2>

                </div>


                <div className="card">

                    <h3>
                        Transaction Amount
                    </h3>

                    <h2>
                        ₹
                        {stats.total_amount || 0}
                    </h2>

                </div>


                <div className="card">

                    <h3>
                        Failed Logins
                    </h3>

                    <h2>
                        {stats.failed_logins || 0}
                    </h2>

                </div>

            </div>


            <section className="chart">

                <h2>
                    Security Activity
                </h2>

                <BarChart
                    width={700}
                    height={350}
                    data={data}
                >

                    <CartesianGrid
                        strokeDasharray="3 3"
                    />

                    <XAxis
                        dataKey="name"
                    />

                    <YAxis />

                    <Tooltip />

                    <Bar
                        dataKey="value"
                    />

                </BarChart>

            </section>

        </main>
    );
}

export default Dashboard;