import React, { useState, useEffect } from 'react';
import './App.css';
import ChatBot from './components/ChatBot';
import ToursList from './components/ToursList';
import Header from './components/Header';
import Hero from './components/Hero';
import { useLanguage } from './i18n/LanguageContext';

function App() {
  const { t } = useLanguage();
  const [tours, setTours] = useState([]);
  const [loading, setLoading] = useState(true);
  const [chatOpen, setChatOpen] = useState(false);

  useEffect(() => {
    fetchTours();
  }, []);

  const fetchTours = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/tours/');
      const data = await response.json();
      setTours(data.results || data);
      setLoading(false);
    } catch (error) {
      console.error('Ошибка загрузки туров:', error);
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <Header />
      <Hero onChatOpen={() => setChatOpen(true)} />
      
      <main className="main-content">
        <section className="tours-section">
          <div className="container">
            <h2>{t('tours.title')}</h2>
            {loading ? (
              <div className="loading">{t('tours.loading')}</div>
            ) : (
              <ToursList tours={tours} />
            )}
          </div>
        </section>
      </main>

      <ChatBot isOpen={chatOpen} onClose={() => setChatOpen(false)} />

      <button 
        className="chat-toggle-btn"
        onClick={() => setChatOpen(!chatOpen)}
        aria-label="Открыть чат с помощником"
      >
        💬
      </button>

      <footer className="footer">
        <div className="container">
          <p>{t('footer.copyright')}</p>
        </div>
      </footer>
    </div>
  );
}

export default App;