class CreateTeamMemberConnections < ActiveRecord::Migration[5.1]
  def change
    create_table :team_member_connections do |t|
      t.integer :member_id
      t.integer :team_id

      t.timestamps
    end
  end
end
