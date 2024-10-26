import React from 'react';
import './App.css';
import Header from './components/Header';
import Breadcrumb from './components/Breadcrumb';
import GSTForm from './components/GSTForm';

function App() {
    return (
        <div className="app">
            <Header />
            <Breadcrumb />
            <GSTForm />
        </div>
    );
}

export default App;
