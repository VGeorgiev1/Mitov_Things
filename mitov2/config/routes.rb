Rails.application.routes.draw do
  resources :team_member_connections
  resources :teams, path: '/B_20_Pesho_Milev_connections'
  resources :members
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
