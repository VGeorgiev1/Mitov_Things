class TeamMemberConnectionsController < ApplicationController
  before_action :set_team_member_connection, only: [:show, :edit, :update, :destroy]

  # GET /team_member_connections
  # GET /team_member_connections.json
  def index
    @team_member_connections = TeamMemberConnection.all
  end

  # GET /team_member_connections/1
  # GET /team_member_connections/1.json
  def show
  end

  # GET /team_member_connections/new
  def new
    @team_member_connection = TeamMemberConnection.new
  end

  # GET /team_member_connections/1/edit
  def edit
  end

  # POST /team_member_connections
  # POST /team_member_connections.json
  def create
    @team_member_connection = TeamMemberConnection.new(team_member_connection_params)

    respond_to do |format|
      if @team_member_connection.save
        format.html { redirect_to @team_member_connection, notice: 'Team member connection was successfully created.' }
        format.json { render :show, status: :created, location: @team_member_connection }
      else
        format.html { render :new }
        format.json { render json: @team_member_connection.errors, status: :unprocessable_entity }
      end
    end
  end

  # PATCH/PUT /team_member_connections/1
  # PATCH/PUT /team_member_connections/1.json
  def update
    respond_to do |format|
      if @team_member_connection.update(team_member_connection_params)
        format.html { redirect_to @team_member_connection, notice: 'Team member connection was successfully updated.' }
        format.json { render :show, status: :ok, location: @team_member_connection }
      else
        format.html { render :edit }
        format.json { render json: @team_member_connection.errors, status: :unprocessable_entity }
      end
    end
  end

  # DELETE /team_member_connections/1
  # DELETE /team_member_connections/1.json
  def destroy
    @team_member_connection.destroy
    respond_to do |format|
      format.html { redirect_to team_member_connections_url, notice: 'Team member connection was successfully destroyed.' }
      format.json { head :no_content }
    end
  end

  private
    # Use callbacks to share common setup or constraints between actions.
    def set_team_member_connection
      @team_member_connection = TeamMemberConnection.find(params[:id])
    end

    # Never trust parameters from the scary internet, only allow the white list through.
    def team_member_connection_params
      params.require(:team_member_connection).permit(:member_id, :team_id)
    end
end
