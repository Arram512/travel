import React from 'react';
import './Hero.css';
import { useLanguage } from '../i18n/LanguageContext';

const Hero = ({ onChatOpen }) => {
  const { t } = useLanguage();
  
  return (
    <section className="hero">
      <div className="hero-overlay"></div>
      <div className="container">
        <div className="hero-content">
          <h1 className="hero-title">{t('hero.title')}</h1>
          <p className="hero-subtitle">{t('hero.subtitle')}</p>
          <div className="hero-actions">
            <button className="btn-primary" onClick={onChatOpen}>
              {t('hero.aiButton')}
            </button>
            <button className="btn-secondary">{t('hero.allToursButton')}</button>
          </div>
          
          <div className="hero-features">
            <div className="feature">
              <span className="feature-icon">🌍</span>
              <span>{t('hero.features.destinations')}</span>
            </div>
            <div className="feature">
              <span className="feature-icon">⭐</span>
              <span>{t('hero.features.hotels')}</span>
            </div>
            <div className="feature">
              <span className="feature-icon">💰</span>
              <span>{t('hero.features.prices')}</span>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
