require 'test_helper'

class TeamMemberConnectionsControllerTest < ActionDispatch::IntegrationTest
  setup do
    @team_member_connection = team_member_connections(:one)
  end

  test "should get index" do
    get team_member_connections_url
    assert_response :success
  end

  test "should get new" do
    get new_team_member_connection_url
    assert_response :success
  end

  test "should create team_member_connection" do
    assert_difference('TeamMemberConnection.count') do
      post team_member_connections_url, params: { team_member_connection: { member_id: @team_member_connection.member_id, team_id: @team_member_connection.team_id } }
    end

    assert_redirected_to team_member_connection_url(TeamMemberConnection.last)
  end

  test "should show team_member_connection" do
    get team_member_connection_url(@team_member_connection)
    assert_response :success
  end

  test "should get edit" do
    get edit_team_member_connection_url(@team_member_connection)
    assert_response :success
  end

  test "should update team_member_connection" do
    patch team_member_connection_url(@team_member_connection), params: { team_member_connection: { member_id: @team_member_connection.member_id, team_id: @team_member_connection.team_id } }
    assert_redirected_to team_member_connection_url(@team_member_connection)
  end

  test "should destroy team_member_connection" do
    assert_difference('TeamMemberConnection.count', -1) do
      delete team_member_connection_url(@team_member_connection)
    end

    assert_redirected_to team_member_connections_url
  end
end
