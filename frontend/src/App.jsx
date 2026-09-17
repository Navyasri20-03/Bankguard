import {
    BrowserRouter,
    Routes,
    Route,
    Link
} from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Transactions from "./pages/Transactions";
import Logins from "./pages/Logins";

import "./index.css";


function App() {

    return (

        <BrowserRouter>

            <div className="app">

                <nav>

                    <h2>🛡 BankGuard AI</h2>

                    <div>

                        <Link to="/">
                            Dashboard
                        </Link>

                        <Link to="/transactions">
                            Transactions
                        </Link>

                        <Link to="/logins">
                            Login Security
                        </Link>

                    </div>

                </nav>


                <Routes>

                    <Route
                        path="/"
                        element={<Dashboard />}
                    />

                    <Route
                        path="/transactions"
                        element={<Transactions />}
                    />

                    <Route
                        path="/logins"
                        element={<Logins />}
                    />

                </Routes>

            </div>

        </BrowserRouter>
    );
}

export default App;