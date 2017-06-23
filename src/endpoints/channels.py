from src.endpoints.base import Base
from src.endpoints.teams import Teams
from src.endpoints.users import Users


class Posts(Base):
	endpoint = '/channels'

	def create_channel(self, options):
		return self.client.post(
			self.endpoint,
			options=options
		)

	def create_direct_message_channel(self, options):
		return self.client.post(
			self.endpoint + '/direct',
			options=options
		)

	def create_group_message_channel(self, options):
		return self.client.post(
			self.endpoint + '/group',
			options=options
		)

	def get_list_of_channels_by_ids(self, team_id, options=None):
		return self.client.post(
			Teams.endpoint + '/' + team_id + '/channels/ids',
			options=options
		)

	def get_channel(self, channel_id):
		return self.client.get(
			self.endpoint + '/' + channel_id
		)

	def update_channel(self, channel_id, options):
		return self.client.put(
			self.endpoint + '/' + channel_id,
			options=options
		)

	def delete_channel(self, channel_id):
		return self.client.delete(
			self.endpoint + '/' + channel_id
		)

	def patch_channel(self, channel_id, options):
		return self.client.put(
			self.endpoint + '/' + channel_id + '/patch',
			options=options
		)

	def restore_channel(self, channel_id):
		return self.client.post(
			self.endpoint + '/' + channel_id + '/restore',
		)

	def get_channel_statistics(self, channel_id):
		return self.client.get(
			self.endpoint + '/' + channel_id + '/stats',
		)

	def get_channel_pinned_posts(self, channel_id):
		return self.client.get(
			self.endpoint + '/' + channel_id + '/pinned'
		)

	def get_channel_by_name(self, team_id, channel_name):
		return self.client.get(
			Teams.endpoint + '/' + team_id + '/channels/name/' + channel_name
		)

	def get_channel_by_name_and_team_name(self, team_name, channel_name):
		return self.client.get(
			Teams.endpoint + '/name/' + team_name + '/channels/name/' + channel_name
		)

	def get_channel_members(self, channel_id, params=None):
		return self.client.get(
			self.endpoint + '/' + channel_id + '/members',
			params=params
		)

	def add_user(self, channel_id, options=None):
		return self.client.post(
			self.endpoint + '/' + channel_id + '/members',
			options=options
		)

	def get_channel_members_by_ids(self, channel_id, options=None):
		return self.client.post(
			self.endpoint + '/' + channel_id + '/members/ids',
			options=options
		)

	def get_channel_member(self, channel_id, user_id):
		return self.client.get(
			self.endpoint + '/' + channel_id + '/members/' + user_id
		)

	def remove_channel_member(self, channel_id, user_id):
		return self.client.delete(
			self.endpoint + '/' + channel_id + '/members/' + user_id
		)

	def update_channel_roles(self, channel_id, user_id, options):
		return self.client.put(
			self.endpoint + '/' + channel_id + '/members/' + user_id + '/roles',
			options=options
		)

	def update_channel_notifications(self, channel_id, user_id, options=None):
		return self.client.put(
			self.endpoint + '/' + channel_id + '/members/' + user_id + '/notify_props',
			options=options
		)

	def view_channel(self, user_id, options):
		return self.client.post(
			self.endpoint + '/members/' + user_id + '/view',
			options=options
		)

	def get_channel_members_for_user(self, user_id, team_id):
		return self.client.get(
			Users.endpoint + '/' + user_id + '/teams/' + team_id + '/channels/members'
		)

	def get_channel_for_user(self, user_id, team_id):
		return self.client.get(
			Users.endpoint + '/' + user_id + '/teams/' + team_id + '/channels'
		)

	def get_unread_messages(self, user_id, channel_id):
		return self.client.get(
			Users.endpoint + '/' + user_id + '/channels/' + channel_id + '/unread'
		)
