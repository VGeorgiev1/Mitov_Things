class CreateCars < ActiveRecord::Migration[5.1]
  def change
    create_table :cars do |t|
      t.integer :number
      t.string :model
      t.timestamp :date
      t.integer :manufactor_id

      t.timestamps
    end
  end
end
