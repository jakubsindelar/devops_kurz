FROM ruby:2.2
RUN mkdir /app
WORKDIR /app
ADD Gemfile /app/Gemfile
ADD app.rb /app
ADD config.ru  /app
ADD lib /app
ADD public /app
ADD views /app
ADD tmp /app
#ADD Gemfile.lock /app/Gemfile.lock
RUN bundle install
