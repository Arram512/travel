import React from 'react';
import './Header.css';
import { useLanguage } from '../i18n/LanguageContext';

const Header = () => {
  const { t, language, toggleLanguage } = useLanguage();
  
  return (
    <header className="header">
      <div className="container">
        <div className="header-content">
          <div className="logo">
            <span className="logo-icon">✈️</span>
            <span className="logo-text">{t('header.logo')}</span>
          </div>
          
          <nav className="nav">
            <a href="#tours">{t('header.nav.tours')}</a>
            <a href="#about">{t('header.nav.about')}</a>
            <a href="#contacts">{t('header.nav.contacts')}</a>
          </nav>
          
          <div className="header-actions">
            <button 
              className="language-toggle" 
              onClick={toggleLanguage}
              title={language === 'ru' ? 'Switch to English' : 'Переключить на русский'}
            >
              {language === 'ru' ? '🇬🇧 EN' : '🇷🇺 RU'}
            </button>
            <button className="btn-secondary">{t('header.login')}</button>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
